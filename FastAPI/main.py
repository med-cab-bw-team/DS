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
async def index(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {"request": request,
        "title": "Welcome to the GardenAPI"}
    )


@api.post("/recommendation")
async def predict(request: Request):
    # modeling happens here
    form = await request.form()
    pred = form["pred"]
    return templates.TemplateResponse(
        "pred.html",
        {"request": request,
         "pred": pred}
    )