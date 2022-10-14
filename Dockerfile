FROM python:3.10-slim-buster

RUN apt update && apt upgrade

WORKDIR /app

COPY service_api service_api
COPY manage.py manage.py
COPY requirements/requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
