# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["uvicorn", "main:app", "--reload", "--port", "5000", "--host", "0.0.0.0"]