FROM python:3.11.9-slim-bullseye

WORKDIR /app

# Install all dependencies 
RUN apt-get update

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8080