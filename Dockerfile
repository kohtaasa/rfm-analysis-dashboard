FROM --platform=linux/amd64 python:3.9-slim

ENV APP_HOME /app
ENV PYTHONUNBUFFERED True
WORKDIR $APP_HOME

COPY . .

USER root

RUN apt-get update

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8050

CMD exec gunicorn --bind :8050 --log-level info --workers 1 --threads 8 --timeout 0 app:server