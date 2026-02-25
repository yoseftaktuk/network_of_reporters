from fastapi import APIRouter, HTTPException
from data_loader import loop_in_file

route = APIRouter()


@route.post('/post_to_kafka')
def start():
    try:
        loop_in_file('data')
        return {'massege': 'The sending was successful.'}
    except HTTPException as e:
        raise str(e)    