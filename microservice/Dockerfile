FROM python:3.8

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /microservice

COPY . /microservice/

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH /microservice

ADD cache-async-few-threads-microservice.py cache-async-few-threads-microservice.py