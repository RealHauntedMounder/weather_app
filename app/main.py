from fastapi import FastAPI
import pandas as pd
import httpx
import openmeteo_requests
import requests_cache
from retry_requests import retry
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class WeatherRequest(BaseModel):
    name: str
    count: int = 10
    format: str = "json"

@app.post("/get_weather") 
async def get_weather(req: WeatherRequest):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": req.name,
                "count": 10,
                "format": "json"
            }
        )
        data = response.json()
        
    if "results" in data and len(data["results"]) > 0:
      first_result = data["results"][0]
      latitude = first_result["latitude"]
      longitude = first_result["longitude"]
    else:
       return 'Город не найден'

    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation_probability,windspeed_10m,snowfall,rain",
    "timezone": "auto"
}

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    hourly = response.Hourly()


    date_range = pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )

    hourly_data = {
        "date": date_range,
        "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
        "relative_humidity_2m": hourly.Variables(1).ValuesAsNumpy(),
        "precipitation_probability": hourly.Variables(2).ValuesAsNumpy(),
        "windspeed_10m": hourly.Variables(3).ValuesAsNumpy(),
        "snowfall": hourly.Variables(4).ValuesAsNumpy(),
        "rain": hourly.Variables(5).ValuesAsNumpy(),
    }

    hourly_dataframe = pd.DataFrame(hourly_data)
    hourly_dataframe["date"] = hourly_dataframe["date"].dt.strftime('%Y-%m-%d %H:%M:%S')

    return {
        "город": req.name,
        "погода": hourly_dataframe.to_dict(orient="records")
    }

