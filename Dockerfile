FROM python:3.11-slim

RUN mkdir /app

RUN apt update && apt install vim -y

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY toupletown/ /app

WORKDIR /app

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "toupletown.asgi:application"]