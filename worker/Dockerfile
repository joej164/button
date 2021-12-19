# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["rq", "worker", "--with-scheduler", "--url", "redis://redis:6379"]
