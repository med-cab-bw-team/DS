"""Main file to drive the API"""
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from .my_jinja import templates, mount_static_directory

api = FastAPI()
mount_static_directory(api)

origins = [
    "http://localhost",
    "https://your-page-here"
]

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
    # modeling happens here
    return {"result": string_of_text}