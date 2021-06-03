# Dockerfile, Image, Container

FROM python:3.8

WORKDIR /poetry-test

COPY ./sandbox ./sandbox

RUN pip install poetry

ENTRYPOINT "make test"