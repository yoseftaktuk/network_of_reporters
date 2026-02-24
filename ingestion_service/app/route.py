from fastapi import APIRouter, HTTPException
from data_loader import loop_in_file

route = APIRouter()

@route.get('/start')
def start():
    pass

@route.post('/post_to_kafka')
def send_to_kafka():
    loop_in_file('data')