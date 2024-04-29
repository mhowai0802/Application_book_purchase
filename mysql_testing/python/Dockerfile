# NOTE name need to be Dockerfile
FROM python:3.10

WORKDIR /create-table

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .