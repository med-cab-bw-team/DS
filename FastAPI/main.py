"""Main file to drive the API"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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


@api.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("base.html",
                                      {"request": request,
                                       "title": "Welcome to the GardenAPI"})


@api.get("/recommendations/{types}&{flavor}&{effect}")
def recommendations(types, flavor, effect):
    form_inputs = {
        "types": types,
        "flavor": flavor,
        "effect": effect}
    # modeling happens here
    return form_inputs
