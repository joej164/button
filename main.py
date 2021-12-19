from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

from datetime import datetime, timedelta
from dotenv import dotenv_values
from helpers import send_push, queue_message, redis_queue_status

import time


config = dotenv_values(".env")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse('images/favicon.ico')


@app.get("/washer")
def washer():
    queue_message(message='Washer is done!!!', wait_time=60)
    queue_message(message='Washer is done!!! - Second Reminder', wait_time=61)
    queue_message(message='Washer is done!!! - Final Reminder', wait_time=65)
    send_push(message='Washer reminders queued!!!')
    return "Washer alarm set"


@app.get("/teapot")
def teapot():
    return FileResponse('images/NPC_Tubby_Rank_7.png', status_code=418)


@app.get("/status")
def status():
    return redis_queue_status()
