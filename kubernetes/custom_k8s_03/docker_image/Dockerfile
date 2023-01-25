#syntax=docker/dockerfile:1

FROM python:3.10.5-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

#Port exposure
EXPOSE 5000

CMD [ "python3", "app.py"]