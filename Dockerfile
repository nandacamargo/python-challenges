FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade

WORKDIR /app

COPY requirements.txt ./
COPY src ./
RUN pip install --upgrade pip && \
  pip install -r requirements.txt

