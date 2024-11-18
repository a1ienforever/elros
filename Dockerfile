FROM python:3.12-alpine

RUN apk update && apk add --no-cache build-base postgresql-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app