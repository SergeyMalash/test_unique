FROM debian:11-slim

RUN mkdir /code

WORKDIR /code

RUN apt update && apt install -y python3 gettext python3-pip libpq-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .