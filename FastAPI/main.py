"""Main file to drive the API"""
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# testing ##
from pydantic import BaseModel
class Data(BaseModel):
    user: str

api = FastAPI()

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

api.mount("/static", StaticFiles(directory="FastAPI/static"), name="static")

templates = Jinja2Templates(directory="FastAPI/templates")


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