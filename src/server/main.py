import os
from fastapi import FastAPI
from pydantic import BaseModel
from FCM import FCM
from FIREBASE_ADMIN import FirebaseAdmin

FMC_FIREBASE_API_SECRET_KEY = os.environ["FMC_FIREBASE_API_SECRET_KEY"]
app = FastAPI()


class SingleData(BaseModel):
    token: str
    title: str
    body: str


class MultiData(BaseModel):
    tokens: list
    title: str
    body: str


@app.post("/FCM/single")
async def fcm_single(data: SingleData):
    fcm = FCM(FMC_FIREBASE_API_SECRET_KEY)
    result = fcm.send_single(
        data.token,
        data.title,
        data.body
    )
    return {
        "result": "success",
        "data": result
    }


@app.get("/FCM/multi")
async def fcm_multi():
    fcm = FCM(FMC_FIREBASE_API_SECRET_KEY)
    result = fcm.send_multi(
        "FCM Multi Test",
        "Test body"
    )
    return {
        "result": "success",
        "data": result
    }


@app.post("/FIREBASE_ADMIN/single")
async def firebase_admin_single(data: SingleData):
    firebase_admin = FirebaseAdmin()
    result = firebase_admin.send_single(
        data.token,
        data.title,
        data.body
    )
    return {
        "result": "success",
        "data": result
    }


@app.post("/FIREBASE_ADMIN/multi")
async def firebase_admin_multi(data: MultiData):
    firebase_admin = FirebaseAdmin()
    result = firebase_admin.send_multi(
        data.tokens,
        data.title,
        data.body
    )
    return {
        "result": "success",
        "data": result
    }

@app.get("/FIREBASE_ADMIN/topic")
async def firebase_admin_topic():
    firebase_admin = FirebaseAdmin()
    result = firebase_admin.send_topic(
        "test",
        "title",
        "content"
    )
    return {
        "result": "success",
        "data": result
    }
