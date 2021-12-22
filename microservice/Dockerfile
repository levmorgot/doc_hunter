FROM python:3.8

WORKDIR /microservice

COPY . /microservice/

RUN pip install --upgrade pip
RUN python -m pip install fastapi httpx gunicorn uvicorn uvloop httptools aioredis arrow

ENV PYTHONPATH /microservice

ADD cache-async-few-threads-microservice.py cache-async-few-threads-microservice.py