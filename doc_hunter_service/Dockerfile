FROM python:3.8

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /doc_hunter_service

COPY . /doc_hunter_service/

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH /microservice

ADD doc_hunter_service.py doc_hunter_service.py