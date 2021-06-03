# Dockerfile, Image, Container

FROM python:3.8

WORKDIR /usr/app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ENV PATH /root/.local/bin:$PATH

COPY ./poetry.lock /usr/app
COPY ./pyproject.toml /usr/app

RUN poetry config virtualenvs.create false && poetry update && poetry install

COPY . /usr/app
