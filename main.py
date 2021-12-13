from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

from datetime import datetime
from dotenv import dotenv_values

import requests

config = dotenv_values(".env")

print(config)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/washer")
def washer():
    url = "https://api.pushover.net/1/messages.json"

    payload = {'user': config['PUSHOVER_USER'],
               'message': f'im a teapot.  it is now {datetime.now()}',
               'token': config['API_TOKEN']}

    response = requests.request("POST", url, data=payload)

    print(response.text)
    return ''


@app.get("/teapot")
def teapot():
    return FileResponse('images/NPC_Tubby_Rank_7.png', status_code=418)
