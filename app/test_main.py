from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_weather_nonexistent_location():
  response = client.post("/get_weather/", json={"name": "moscoww",
                "count": 10,
                "format": "json"})
  assert response.status_code == 200
  assert response.json() == 'Город не найден'


def test_get_weather_existent_location():
    response = client.post("/get_weather/", json={"name": "moscow",
                "count": 10,
                "format": "json"})
    assert response.status_code == 200
    assert response.json() == {
       
  "город": "moscow",
  "погода": [
    {
      "date": "2025-05-26 21:00:00",
      "temperature_2m": 19.98900032043457,
      "relative_humidity_2m": 44,
      "precipitation_probability": 0,
      "windspeed_10m": 5.9044389724731445,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-26 22:00:00",
      "temperature_2m": 19.18899917602539,
      "relative_humidity_2m": 48,
      "precipitation_probability": 0,
      "windspeed_10m": 5.9044389724731445,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-26 23:00:00",
      "temperature_2m": 18.588998794555664,
      "relative_humidity_2m": 50,
      "precipitation_probability": 0,
      "windspeed_10m": 6.792466163635254,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 00:00:00",
      "temperature_2m": 18.338998794555664,
      "relative_humidity_2m": 51,
      "precipitation_probability": 0,
      "windspeed_10m": 6.92473840713501,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 01:00:00",
      "temperature_2m": 17.788999557495117,
      "relative_humidity_2m": 53,
      "precipitation_probability": 0,
      "windspeed_10m": 7.2448601722717285,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 02:00:00",
      "temperature_2m": 17.338998794555664,
      "relative_humidity_2m": 54,
      "precipitation_probability": 0,
      "windspeed_10m": 7.1003098487854,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 03:00:00",
      "temperature_2m": 18.038999557495117,
      "relative_humidity_2m": 50,
      "precipitation_probability": 0,
      "windspeed_10m": 7.289444923400879,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 04:00:00",
      "temperature_2m": 18.68899917602539,
      "relative_humidity_2m": 47,
      "precipitation_probability": 0,
      "windspeed_10m": 9.504273414611816,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 05:00:00",
      "temperature_2m": 19.888999938964844,
      "relative_humidity_2m": 44,
      "precipitation_probability": 0,
      "windspeed_10m": 9.199390411376953,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 06:00:00",
      "temperature_2m": 22.48900032043457,
      "relative_humidity_2m": 32,
      "precipitation_probability": 0,
      "windspeed_10m": 11.384199142456055,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 07:00:00",
      "temperature_2m": 23.93899917602539,
      "relative_humidity_2m": 27,
      "precipitation_probability": 3,
      "windspeed_10m": 12.31389331817627,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 08:00:00",
      "temperature_2m": 24.838998794555664,
      "relative_humidity_2m": 21,
      "precipitation_probability": 3,
      "windspeed_10m": 13.661038398742676,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 09:00:00",
      "temperature_2m": 24.93899917602539,
      "relative_humidity_2m": 21,
      "precipitation_probability": 0,
      "windspeed_10m": 14.182354927062988,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 10:00:00",
      "temperature_2m": 25.288999557495117,
      "relative_humidity_2m": 20,
      "precipitation_probability": 0,
      "windspeed_10m": 13.5706148147583,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 11:00:00",
      "temperature_2m": 25.73900032043457,
      "relative_humidity_2m": 20,
      "precipitation_probability": 0,
      "windspeed_10m": 13.5706148147583,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 12:00:00",
      "temperature_2m": 26.038999557495117,
      "relative_humidity_2m": 21,
      "precipitation_probability": 0,
      "windspeed_10m": 12.979984283447266,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 13:00:00",
      "temperature_2m": 26.18899917602539,
      "relative_humidity_2m": 21,
      "precipitation_probability": 0,
      "windspeed_10m": 12.303365707397461,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 14:00:00",
      "temperature_2m": 26.088998794555664,
      "relative_humidity_2m": 21,
      "precipitation_probability": 0,
      "windspeed_10m": 11.841755867004395,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 15:00:00",
      "temperature_2m": 25.588998794555664,
      "relative_humidity_2m": 23,
      "precipitation_probability": 0,
      "windspeed_10m": 10.495713233947754,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 16:00:00",
      "temperature_2m": 25.038999557495117,
      "relative_humidity_2m": 24,
      "precipitation_probability": 0,
      "windspeed_10m": 9.504273414611816,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 17:00:00",
      "temperature_2m": 23.98900032043457,
      "relative_humidity_2m": 26,
      "precipitation_probability": 0,
      "windspeed_10m": 6.696386814117432,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 18:00:00",
      "temperature_2m": 22.388999938964844,
      "relative_humidity_2m": 32,
      "precipitation_probability": 0,
      "windspeed_10m": 5.623379707336426,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 19:00:00",
      "temperature_2m": 20.98900032043457,
      "relative_humidity_2m": 37,
      "precipitation_probability": 0,
      "windspeed_10m": 6.130578517913818,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 20:00:00",
      "temperature_2m": 19.888999938964844,
      "relative_humidity_2m": 40,
      "precipitation_probability": 0,
      "windspeed_10m": 6.369049549102783,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 21:00:00",
      "temperature_2m": 18.98900032043457,
      "relative_humidity_2m": 42,
      "precipitation_probability": 0,
      "windspeed_10m": 5.991593837738037,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 22:00:00",
      "temperature_2m": 18.23900032043457,
      "relative_humidity_2m": 43,
      "precipitation_probability": 0,
      "windspeed_10m": 5.804825305938721,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-27 23:00:00",
      "temperature_2m": 17.68899917602539,
      "relative_humidity_2m": 45,
      "precipitation_probability": 0,
      "windspeed_10m": 5.399999618530273,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 00:00:00",
      "temperature_2m": 17.288999557495117,
      "relative_humidity_2m": 47,
      "precipitation_probability": 0,
      "windspeed_10m": 5.091168403625488,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 01:00:00",
      "temperature_2m": 16.73900032043457,
      "relative_humidity_2m": 47,
      "precipitation_probability": 0,
      "windspeed_10m": 5.623379707336426,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 02:00:00",
      "temperature_2m": 16.338998794555664,
      "relative_humidity_2m": 48,
      "precipitation_probability": 0,
      "windspeed_10m": 5.86037540435791,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 03:00:00",
      "temperature_2m": 16.48900032043457,
      "relative_humidity_2m": 47,
      "precipitation_probability": 0,
      "windspeed_10m": 6.369049549102783,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 04:00:00",
      "temperature_2m": 17.138999938964844,
      "relative_humidity_2m": 45,
      "precipitation_probability": 0,
      "windspeed_10m": 7.127635955810547,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 05:00:00",
      "temperature_2m": 18.588998794555664,
      "relative_humidity_2m": 42,
      "precipitation_probability": 0,
      "windspeed_10m": 7.9932966232299805,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 06:00:00",
      "temperature_2m": 20.48900032043457,
      "relative_humidity_2m": 37,
      "precipitation_probability": 0,
      "windspeed_10m": 8.396570205688477,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 07:00:00",
      "temperature_2m": 22.43899917602539,
      "relative_humidity_2m": 34,
      "precipitation_probability": 0,
      "windspeed_10m": 9.387651443481445,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 08:00:00",
      "temperature_2m": 24.23900032043457,
      "relative_humidity_2m": 29,
      "precipitation_probability": 0,
      "windspeed_10m": 10.5142183303833,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 09:00:00",
      "temperature_2m": 25.43899917602539,
      "relative_humidity_2m": 23,
      "precipitation_probability": 0,
      "windspeed_10m": 13.089353561401367,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 10:00:00",
      "temperature_2m": 26.18899917602539,
      "relative_humidity_2m": 21,
      "precipitation_probability": 0,
      "windspeed_10m": 14.168641090393066,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 11:00:00",
      "temperature_2m": 26.73900032043457,
      "relative_humidity_2m": 20,
      "precipitation_probability": 0,
      "windspeed_10m": 13.854154586791992,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 12:00:00",
      "temperature_2m": 27.18899917602539,
      "relative_humidity_2m": 19,
      "precipitation_probability": 0,
      "windspeed_10m": 13.684735298156738,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 13:00:00",
      "temperature_2m": 27.23900032043457,
      "relative_humidity_2m": 20,
      "precipitation_probability": 0,
      "windspeed_10m": 14.007655143737793,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 14:00:00",
      "temperature_2m": 27.088998794555664,
      "relative_humidity_2m": 20,
      "precipitation_probability": 0,
      "windspeed_10m": 13.84947681427002,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 15:00:00",
      "temperature_2m": 26.638999938964844,
      "relative_humidity_2m": 21,
      "precipitation_probability": 0,
      "windspeed_10m": 13.532360076904297,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 16:00:00",
      "temperature_2m": 26.538999557495117,
      "relative_humidity_2m": 22,
      "precipitation_probability": 0,
      "windspeed_10m": 12.239999771118164,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 17:00:00",
      "temperature_2m": 25.388999938964844,
      "relative_humidity_2m": 23,
      "precipitation_probability": 0,
      "windspeed_10m": 10.188699722290039,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 18:00:00",
      "temperature_2m": 23.68899917602539,
      "relative_humidity_2m": 26,
      "precipitation_probability": 0,
      "windspeed_10m": 8.496304512023926,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 19:00:00",
      "temperature_2m": 22.038999557495117,
      "relative_humidity_2m": 30,
      "precipitation_probability": 0,
      "windspeed_10m": 7.4215898513793945,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 20:00:00",
      "temperature_2m": 20.68899917602539,
      "relative_humidity_2m": 34,
      "precipitation_probability": 0,
      "windspeed_10m": 6.792466163635254,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 21:00:00",
      "temperature_2m": 19.43899917602539,
      "relative_humidity_2m": 36,
      "precipitation_probability": 0,
      "windspeed_10m": 5.692099094390869,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 22:00:00",
      "temperature_2m": 18.48900032043457,
      "relative_humidity_2m": 39,
      "precipitation_probability": 0,
      "windspeed_10m": 5.351784706115723,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-28 23:00:00",
      "temperature_2m": 17.838998794555664,
      "relative_humidity_2m": 40,
      "precipitation_probability": 0,
      "windspeed_10m": 4.896529674530029,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 00:00:00",
      "temperature_2m": 17.338998794555664,
      "relative_humidity_2m": 42,
      "precipitation_probability": 0,
      "windspeed_10m": 5.191993713378906,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 01:00:00",
      "temperature_2m": 16.68899917602539,
      "relative_humidity_2m": 44,
      "precipitation_probability": 0,
      "windspeed_10m": 5.804825305938721,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 02:00:00",
      "temperature_2m": 16.338998794555664,
      "relative_humidity_2m": 45,
      "precipitation_probability": 0,
      "windspeed_10m": 5.191993713378906,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 03:00:00",
      "temperature_2m": 16.73900032043457,
      "relative_humidity_2m": 45,
      "precipitation_probability": 0,
      "windspeed_10m": 6.287129878997803,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 04:00:00",
      "temperature_2m": 18.138999938964844,
      "relative_humidity_2m": 41,
      "precipitation_probability": 0,
      "windspeed_10m": 7.594208240509033,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 05:00:00",
      "temperature_2m": 19.98900032043457,
      "relative_humidity_2m": 37,
      "precipitation_probability": 0,
      "windspeed_10m": 8.225034713745117,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 06:00:00",
      "temperature_2m": 21.98900032043457,
      "relative_humidity_2m": 34,
      "precipitation_probability": 0,
      "windspeed_10m": 9.387651443481445,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 07:00:00",
      "temperature_2m": 23.038999557495117,
      "relative_humidity_2m": 33,
      "precipitation_probability": 0,
      "windspeed_10m": 12.229406356811523,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 08:00:00",
      "temperature_2m": 23.18899917602539,
      "relative_humidity_2m": 34,
      "precipitation_probability": 0,
      "windspeed_10m": 11.966954231262207,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 09:00:00",
      "temperature_2m": 25.43899917602539,
      "relative_humidity_2m": 30,
      "precipitation_probability": 0,
      "windspeed_10m": 10.805997848510742,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 10:00:00",
      "temperature_2m": 27.73900032043457,
      "relative_humidity_2m": 25,
      "precipitation_probability": 0,
      "windspeed_10m": 14.00302791595459,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 11:00:00",
      "temperature_2m": 28.68899917602539,
      "relative_humidity_2m": 23,
      "precipitation_probability": 0,
      "windspeed_10m": 15.990646362304688,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 12:00:00",
      "temperature_2m": 29.388999938964844,
      "relative_humidity_2m": 18,
      "precipitation_probability": 0,
      "windspeed_10m": 16.74677276611328,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 13:00:00",
      "temperature_2m": 28.888999938964844,
      "relative_humidity_2m": 18,
      "precipitation_probability": 0,
      "windspeed_10m": 15.937877655029297,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 14:00:00",
      "temperature_2m": 28.23900032043457,
      "relative_humidity_2m": 19,
      "precipitation_probability": 0,
      "windspeed_10m": 14.587776184082031,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 15:00:00",
      "temperature_2m": 27.088998794555664,
      "relative_humidity_2m": 19,
      "precipitation_probability": 0,
      "windspeed_10m": 14.044614791870117,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 16:00:00",
      "temperature_2m": 26.088998794555664,
      "relative_humidity_2m": 17,
      "precipitation_probability": 1,
      "windspeed_10m": 9.007196426391602,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 17:00:00",
      "temperature_2m": 25.038999557495117,
      "relative_humidity_2m": 21,
      "precipitation_probability": 2,
      "windspeed_10m": 2.6208393573760986,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 18:00:00",
      "temperature_2m": 24.088998794555664,
      "relative_humidity_2m": 25,
      "precipitation_probability": 3,
      "windspeed_10m": 2.4149534702301025,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 19:00:00",
      "temperature_2m": 23.23900032043457,
      "relative_humidity_2m": 27,
      "precipitation_probability": 2,
      "windspeed_10m": 2.5199999809265137,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 20:00:00",
      "temperature_2m": 22.588998794555664,
      "relative_humidity_2m": 28,
      "precipitation_probability": 1,
      "windspeed_10m": 0.7199999690055847,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 21:00:00",
      "temperature_2m": 21.788999557495117,
      "relative_humidity_2m": 30,
      "precipitation_probability": 0,
      "windspeed_10m": 3.096837043762207,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 22:00:00",
      "temperature_2m": 20.98900032043457,
      "relative_humidity_2m": 33,
      "precipitation_probability": 1,
      "windspeed_10m": 3.415259599685669,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-29 23:00:00",
      "temperature_2m": 20.68899917602539,
      "relative_humidity_2m": 35,
      "precipitation_probability": 2,
      "windspeed_10m": 2.9024126529693604,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 00:00:00",
      "temperature_2m": 19.588998794555664,
      "relative_humidity_2m": 33,
      "precipitation_probability": 3,
      "windspeed_10m": 5.937272071838379,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 01:00:00",
      "temperature_2m": 19.038999557495117,
      "relative_humidity_2m": 36,
      "precipitation_probability": 3,
      "windspeed_10m": 8.55710220336914,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 02:00:00",
      "temperature_2m": 19.288999557495117,
      "relative_humidity_2m": 35,
      "precipitation_probability": 3,
      "windspeed_10m": 3.3190360069274902,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 03:00:00",
      "temperature_2m": 19.038999557495117,
      "relative_humidity_2m": 37,
      "precipitation_probability": 3,
      "windspeed_10m": 5.804825305938721,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 04:00:00",
      "temperature_2m": 19.48900032043457,
      "relative_humidity_2m": 39,
      "precipitation_probability": 7,
      "windspeed_10m": 5.815978050231934,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 05:00:00",
      "temperature_2m": 20.138999938964844,
      "relative_humidity_2m": 39,
      "precipitation_probability": 7,
      "windspeed_10m": 7.491114139556885,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 06:00:00",
      "temperature_2m": 21.088998794555664,
      "relative_humidity_2m": 38,
      "precipitation_probability": 8,
      "windspeed_10m": 5.991593837738037,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 07:00:00",
      "temperature_2m": 22.138999938964844,
      "relative_humidity_2m": 39,
      "precipitation_probability": 8,
      "windspeed_10m": 8.31124496459961,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 08:00:00",
      "temperature_2m": 22.788999557495117,
      "relative_humidity_2m": 39,
      "precipitation_probability": 9,
      "windspeed_10m": 11.879999160766602,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 09:00:00",
      "temperature_2m": 22.638999938964844,
      "relative_humidity_2m": 43,
      "precipitation_probability": 9,
      "windspeed_10m": 12.661563873291016,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 10:00:00",
      "temperature_2m": 22.588998794555664,
      "relative_humidity_2m": 50,
      "precipitation_probability": 9,
      "windspeed_10m": 12.397806167602539,
      "snowfall": 0,
      "rain": 0.10000000149011612
    },
    {
      "date": "2025-05-30 11:00:00",
      "temperature_2m": 23.838998794555664,
      "relative_humidity_2m": 45,
      "precipitation_probability": 9,
      "windspeed_10m": 14.764389038085938,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 12:00:00",
      "temperature_2m": 24.48900032043457,
      "relative_humidity_2m": 41,
      "precipitation_probability": 8,
      "windspeed_10m": 12.0693998336792,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 13:00:00",
      "temperature_2m": 24.838998794555664,
      "relative_humidity_2m": 40,
      "precipitation_probability": 7,
      "windspeed_10m": 11.726277351379395,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 14:00:00",
      "temperature_2m": 25.038999557495117,
      "relative_humidity_2m": 38,
      "precipitation_probability": 5,
      "windspeed_10m": 10.661107063293457,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 15:00:00",
      "temperature_2m": 24.838998794555664,
      "relative_humidity_2m": 39,
      "precipitation_probability": 3,
      "windspeed_10m": 10.137691497802734,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 16:00:00",
      "temperature_2m": 24.088998794555664,
      "relative_humidity_2m": 44,
      "precipitation_probability": 1,
      "windspeed_10m": 9.720000267028809,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 17:00:00",
      "temperature_2m": 22.98900032043457,
      "relative_humidity_2m": 51,
      "precipitation_probability": 0,
      "windspeed_10m": 9.779816627502441,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 18:00:00",
      "temperature_2m": 21.888999938964844,
      "relative_humidity_2m": 57,
      "precipitation_probability": 0,
      "windspeed_10m": 9.114471435546875,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 19:00:00",
      "temperature_2m": 20.93899917602539,
      "relative_humidity_2m": 61,
      "precipitation_probability": 1,
      "windspeed_10m": 7.594207286834717,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 20:00:00",
      "temperature_2m": 19.98900032043457,
      "relative_humidity_2m": 64,
      "precipitation_probability": 3,
      "windspeed_10m": 6.130578994750977,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 21:00:00",
      "temperature_2m": 19.23900032043457,
      "relative_humidity_2m": 67,
      "precipitation_probability": 6,
      "windspeed_10m": 4.802999019622803,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 22:00:00",
      "temperature_2m": 18.68899917602539,
      "relative_humidity_2m": 69,
      "precipitation_probability": 8,
      "windspeed_10m": 3.7585103511810303,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-30 23:00:00",
      "temperature_2m": 18.288999557495117,
      "relative_humidity_2m": 70,
      "precipitation_probability": 11,
      "windspeed_10m": 3.3190360069274902,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 00:00:00",
      "temperature_2m": 17.98900032043457,
      "relative_humidity_2m": 70,
      "precipitation_probability": 13,
      "windspeed_10m": 2.6208393573760986,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 01:00:00",
      "temperature_2m": 17.838998794555664,
      "relative_humidity_2m": 70,
      "precipitation_probability": 14,
      "windspeed_10m": 1.9386591911315918,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 02:00:00",
      "temperature_2m": 17.788999557495117,
      "relative_humidity_2m": 69,
      "precipitation_probability": 15,
      "windspeed_10m": 1.6099690198898315,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 03:00:00",
      "temperature_2m": 17.838998794555664,
      "relative_humidity_2m": 68,
      "precipitation_probability": 16,
      "windspeed_10m": 1.527350664138794,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 04:00:00",
      "temperature_2m": 17.93899917602539,
      "relative_humidity_2m": 69,
      "precipitation_probability": 16,
      "windspeed_10m": 1.7999999523162842,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 05:00:00",
      "temperature_2m": 18.088998794555664,
      "relative_humidity_2m": 70,
      "precipitation_probability": 17,
      "windspeed_10m": 2.3051247596740723,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 06:00:00",
      "temperature_2m": 18.538999557495117,
      "relative_humidity_2m": 70,
      "precipitation_probability": 18,
      "windspeed_10m": 3.054701328277588,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 07:00:00",
      "temperature_2m": 19.48900032043457,
      "relative_humidity_2m": 67,
      "precipitation_probability": 19,
      "windspeed_10m": 4.33497428894043,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 08:00:00",
      "temperature_2m": 20.68899917602539,
      "relative_humidity_2m": 62,
      "precipitation_probability": 21,
      "windspeed_10m": 5.86037540435791,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 09:00:00",
      "temperature_2m": 21.638999938964844,
      "relative_humidity_2m": 58,
      "precipitation_probability": 23,
      "windspeed_10m": 7.199999809265137,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 10:00:00",
      "temperature_2m": 22.038999557495117,
      "relative_humidity_2m": 55,
      "precipitation_probability": 25,
      "windspeed_10m": 8.049844741821289,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 11:00:00",
      "temperature_2m": 22.18899917602539,
      "relative_humidity_2m": 53,
      "precipitation_probability": 27,
      "windspeed_10m": 8.55710220336914,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 12:00:00",
      "temperature_2m": 22.18899917602539,
      "relative_humidity_2m": 53,
      "precipitation_probability": 28,
      "windspeed_10m": 9.114471435546875,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 13:00:00",
      "temperature_2m": 22.038999557495117,
      "relative_humidity_2m": 55,
      "precipitation_probability": 29,
      "windspeed_10m": 8.55710220336914,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 14:00:00",
      "temperature_2m": 21.73900032043457,
      "relative_humidity_2m": 58,
      "precipitation_probability": 29,
      "windspeed_10m": 7.895416259765625,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 15:00:00",
      "temperature_2m": 21.388999938964844,
      "relative_humidity_2m": 62,
      "precipitation_probability": 29,
      "windspeed_10m": 6.989935874938965,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 16:00:00",
      "temperature_2m": 20.98900032043457,
      "relative_humidity_2m": 66,
      "precipitation_probability": 29,
      "windspeed_10m": 5.991593837738037,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 17:00:00",
      "temperature_2m": 20.43899917602539,
      "relative_humidity_2m": 70,
      "precipitation_probability": 29,
      "windspeed_10m": 4.680000305175781,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 18:00:00",
      "temperature_2m": 19.838998794555664,
      "relative_humidity_2m": 71,
      "precipitation_probability": 28,
      "windspeed_10m": 3.415259599685669,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 19:00:00",
      "temperature_2m": 19.038999557495117,
      "relative_humidity_2m": 66,
      "precipitation_probability": 26,
      "windspeed_10m": 2.811689853668213,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 20:00:00",
      "temperature_2m": 18.138999938964844,
      "relative_humidity_2m": 57,
      "precipitation_probability": 24,
      "windspeed_10m": 3.976329803466797,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 21:00:00",
      "temperature_2m": 17.23900032043457,
      "relative_humidity_2m": 52,
      "precipitation_probability": 22,
      "windspeed_10m": 5.447788238525391,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 22:00:00",
      "temperature_2m": 16.43899917602539,
      "relative_humidity_2m": 53,
      "precipitation_probability": 19,
      "windspeed_10m": 6.287129878997803,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-05-31 23:00:00",
      "temperature_2m": 15.68899917602539,
      "relative_humidity_2m": 57,
      "precipitation_probability": 17,
      "windspeed_10m": 6.6380720138549805,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 00:00:00",
      "temperature_2m": 15.038999557495117,
      "relative_humidity_2m": 62,
      "precipitation_probability": 15,
      "windspeed_10m": 7.072877883911133,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 01:00:00",
      "temperature_2m": 14.288999557495117,
      "relative_humidity_2m": 69,
      "precipitation_probability": 14,
      "windspeed_10m": 7.628262996673584,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 02:00:00",
      "temperature_2m": 13.58899974822998,
      "relative_humidity_2m": 78,
      "precipitation_probability": 13,
      "windspeed_10m": 8.08999252319336,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 03:00:00",
      "temperature_2m": 13.488999366760254,
      "relative_humidity_2m": 81,
      "precipitation_probability": 12,
      "windspeed_10m": 8.55710220336914,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 04:00:00",
      "temperature_2m": 14.43899917602539,
      "relative_humidity_2m": 75,
      "precipitation_probability": 11,
      "windspeed_10m": 9.346142768859863,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 05:00:00",
      "temperature_2m": 15.93899917602539,
      "relative_humidity_2m": 65,
      "precipitation_probability": 10,
      "windspeed_10m": 10.538843154907227,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 06:00:00",
      "temperature_2m": 17.038999557495117,
      "relative_humidity_2m": 57,
      "precipitation_probability": 10,
      "windspeed_10m": 11.54247760772705,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 07:00:00",
      "temperature_2m": 16.92150115966797,
      "relative_humidity_2m": 55,
      "precipitation_probability": 25,
      "windspeed_10m": 10.538843154907227,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 08:00:00",
      "temperature_2m": 17.92150115966797,
      "relative_humidity_2m": 48,
      "precipitation_probability": 27,
      "windspeed_10m": 10.895576477050781,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 09:00:00",
      "temperature_2m": 18.771501541137695,
      "relative_humidity_2m": 43,
      "precipitation_probability": 28,
      "windspeed_10m": 11.304228782653809,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 10:00:00",
      "temperature_2m": 19.471500396728516,
      "relative_humidity_2m": 39,
      "precipitation_probability": 29,
      "windspeed_10m": 11.65977668762207,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 11:00:00",
      "temperature_2m": 20.071500778198242,
      "relative_humidity_2m": 36,
      "precipitation_probability": 30,
      "windspeed_10m": 12.015588760375977,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 12:00:00",
      "temperature_2m": 20.42150115966797,
      "relative_humidity_2m": 34,
      "precipitation_probability": 30,
      "windspeed_10m": 12.015588760375977,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 13:00:00",
      "temperature_2m": 20.521501541137695,
      "relative_humidity_2m": 32,
      "precipitation_probability": 30,
      "windspeed_10m": 12.144330978393555,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 14:00:00",
      "temperature_2m": 20.321500778198242,
      "relative_humidity_2m": 32,
      "precipitation_probability": 29,
      "windspeed_10m": 12.41347599029541,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 15:00:00",
      "temperature_2m": 19.87150001525879,
      "relative_humidity_2m": 32,
      "precipitation_probability": 29,
      "windspeed_10m": 12.303365707397461,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 16:00:00",
      "temperature_2m": 18.971500396728516,
      "relative_humidity_2m": 34,
      "precipitation_probability": 28,
      "windspeed_10m": 11.44097900390625,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 17:00:00",
      "temperature_2m": 17.771501541137695,
      "relative_humidity_2m": 38,
      "precipitation_probability": 27,
      "windspeed_10m": 9.826087951660156,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 18:00:00",
      "temperature_2m": 16.571500778198242,
      "relative_humidity_2m": 42,
      "precipitation_probability": 26,
      "windspeed_10m": 8.396570205688477,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 19:00:00",
      "temperature_2m": 15.421500205993652,
      "relative_humidity_2m": 47,
      "precipitation_probability": 25,
      "windspeed_10m": 6.792466163635254,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 20:00:00",
      "temperature_2m": 14.321499824523926,
      "relative_humidity_2m": 54,
      "precipitation_probability": 24,
      "windspeed_10m": 5.315336227416992,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 21:00:00",
      "temperature_2m": 13.371500015258789,
      "relative_humidity_2m": 59,
      "precipitation_probability": 23,
      "windspeed_10m": 4.213691711425781,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 22:00:00",
      "temperature_2m": 12.621500015258789,
      "relative_humidity_2m": 62,
      "precipitation_probability": 22,
      "windspeed_10m": 4.0249223709106445,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-01 23:00:00",
      "temperature_2m": 12.021499633789062,
      "relative_humidity_2m": 65,
      "precipitation_probability": 21,
      "windspeed_10m": 4.6938252449035645,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 00:00:00",
      "temperature_2m": 11.621500015258789,
      "relative_humidity_2m": 67,
      "precipitation_probability": 20,
      "windspeed_10m": 5.052840709686279,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 01:00:00",
      "temperature_2m": 11.371500015258789,
      "relative_humidity_2m": 69,
      "precipitation_probability": 19,
      "windspeed_10m": 5.411986351013184,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 02:00:00",
      "temperature_2m": 11.271499633789062,
      "relative_humidity_2m": 71,
      "precipitation_probability": 19,
      "windspeed_10m": 5.506940841674805,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 03:00:00",
      "temperature_2m": 11.7214994430542,
      "relative_humidity_2m": 71,
      "precipitation_probability": 18,
      "windspeed_10m": 5.937272071838379,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 04:00:00",
      "temperature_2m": 12.9714994430542,
      "relative_humidity_2m": 67,
      "precipitation_probability": 18,
      "windspeed_10m": 6.489992141723633,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 05:00:00",
      "temperature_2m": 14.671500205993652,
      "relative_humidity_2m": 60,
      "precipitation_probability": 18,
      "windspeed_10m": 7.091177463531494,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 06:00:00",
      "temperature_2m": 16.271501541137695,
      "relative_humidity_2m": 53,
      "precipitation_probability": 17,
      "windspeed_10m": 7.56856632232666,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 07:00:00",
      "temperature_2m": 17.471500396728516,
      "relative_humidity_2m": 47,
      "precipitation_probability": 17,
      "windspeed_10m": 7.4215898513793945,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 08:00:00",
      "temperature_2m": 18.521501541137695,
      "relative_humidity_2m": 41,
      "precipitation_probability": 16,
      "windspeed_10m": 6.725354194641113,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 09:00:00",
      "temperature_2m": 19.471500396728516,
      "relative_humidity_2m": 37,
      "precipitation_probability": 16,
      "windspeed_10m": 6.519876956939697,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 10:00:00",
      "temperature_2m": 20.471500396728516,
      "relative_humidity_2m": 34,
      "precipitation_probability": 16,
      "windspeed_10m": 6.8777899742126465,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 11:00:00",
      "temperature_2m": 21.37150001525879,
      "relative_humidity_2m": 33,
      "precipitation_probability": 15,
      "windspeed_10m": 7.5170207023620605,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 12:00:00",
      "temperature_2m": 22.021501541137695,
      "relative_humidity_2m": 32,
      "precipitation_probability": 15,
      "windspeed_10m": 7.895416259765625,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 13:00:00",
      "temperature_2m": 22.37150001525879,
      "relative_humidity_2m": 30,
      "precipitation_probability": 15,
      "windspeed_10m": 7.903619289398193,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 14:00:00",
      "temperature_2m": 22.42150115966797,
      "relative_humidity_2m": 29,
      "precipitation_probability": 14,
      "windspeed_10m": 7.787990570068359,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 15:00:00",
      "temperature_2m": 22.17150115966797,
      "relative_humidity_2m": 29,
      "precipitation_probability": 14,
      "windspeed_10m": 7.4215898513793945,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 16:00:00",
      "temperature_2m": 21.42150115966797,
      "relative_humidity_2m": 32,
      "precipitation_probability": 13,
      "windspeed_10m": 6.6380720138549805,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 17:00:00",
      "temperature_2m": 20.321500778198242,
      "relative_humidity_2m": 36,
      "precipitation_probability": 13,
      "windspeed_10m": 5.634891033172607,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 18:00:00",
      "temperature_2m": 19.221500396728516,
      "relative_humidity_2m": 40,
      "precipitation_probability": 13,
      "windspeed_10m": 5.154415607452393,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 19:00:00",
      "temperature_2m": 18.071500778198242,
      "relative_humidity_2m": 44,
      "precipitation_probability": 12,
      "windspeed_10m": 5.052840709686279,
      "snowfall": 0,
      "rain": 0
    },
    {
      "date": "2025-06-02 20:00:00",
      "temperature_2m": 16.87150001525879,
      "relative_humidity_2m": 48,
      "precipitation_probability": 12,
      "windspeed_10m": 5.399999618530273,
      "snowfall": 0,
      "rain": 0
    }
  ]
       }
    
