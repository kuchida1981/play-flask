FROM python:3.10-slim-bullseye
WORKDIR /work
COPY . ./
RUN pip install -e .
