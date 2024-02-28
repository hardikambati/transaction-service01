FROM python:3.8.10-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir /service-01

COPY . /service-01/

WORKDIR /service-01

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ['python3', 'main.py']