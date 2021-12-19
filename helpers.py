import requests
import redis

from datetime import datetime, timedelta
from dotenv import dotenv_values
from rq import Queue

config = dotenv_values(".env")
cache = redis.Redis(host='redis', port=6379)
q = Queue(connection=cache)


def redis_queue_status():
    redis_status = cache.ping()
    return redis_status


def queue_message(message: str = 'Default message', wait_time: int = 60) -> requests.Response:
    job = q.enqueue_in(timedelta(minutes=wait_time), send_push, message)
    return job


def send_push(message: str = 'Default message') -> requests.Response:
    url = "https://api.pushover.net/1/messages.json"

    payload = {
        'user': config['PUSHOVER_USER'],
        'message': f'{message}',
        'token': config['API_TOKEN']
    }

    response = requests.request("POST", url, data=payload)
    return response
