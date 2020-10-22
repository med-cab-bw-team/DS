"""Main file to drive the API"""
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from .my_jinja import templates, mount_static_directory
from .model import PredictionBot

api = FastAPI()
mount_static_directory(api)
# api.strain_finder = MODEL()


api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@api.get("/")
async def index():
    return {"welcome"}


@api.get("/recommendation/{string_of_text}")
async def predict(string_of_text):
    recc = api.strain_finder.search(string_of_text)
    return {recc}