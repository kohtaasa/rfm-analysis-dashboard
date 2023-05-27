FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY . .

USER root

RUN apt-get update

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8050

CMD ["python", "app.py"]


