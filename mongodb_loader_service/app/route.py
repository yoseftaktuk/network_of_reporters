from fastapi import APIRouter, HTTPException, Request
from mongodb_connection import MongoDbService

route = APIRouter()
mongo = MongoDbService()
mongo.conect()
mongo.creat_collection()

@route.post('/post_to_mongodb')
async def send_to_kafka(data: Request):
    try:
        data = await data.body()
        mongo.insert_one_preparing(data)
    except HTTPException as e:
        raise str(e)    