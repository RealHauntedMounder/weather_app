Простое веб-приложение на FastAPI, показывающее погоду по введённому городу.

**К приложению написаны тесты, всё помещено в докер контейнер**

В работе использовался JavaScript, FastAPI, HTML, Tailwind CSS, Docker

Для запуска нужно зайти в корневую директорию с проектом и прописать:
1) docker build -t myimage . 
2) docker run -d --name mycontainer -p 8000:8000 myimage
