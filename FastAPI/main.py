"""Main module to drive the API"""
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from .my_jinja import templates, mount_static_directory

tags_metadata = [
    {
        "name": "root",
        "description": "Root directory, Returns brief description",
    },
    {
        "name": "nlpmodel",
        "description": "NLP model endpoint to process strain recommendations",
    },
]

api = FastAPI(
    title="Green Garden API",
    description="This API houses \
        a natural language processing model \
        that returns marijuana strain recommendations \
        based on the users prefrences and necessities.",
    version="0.1.0",
    openapi_tags=tags_metadata)

# Mount the static directory to be used by templates
mount_static_directory(api)


api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


@api.get("/", tags=["root"])
async def index(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {"request": request,
        "title": "Welcome to the Green Garden API"})


@api.get(
    "/recommendation/{string_to_process}",
    tags=["nlpmodel"])
async def predict(string_to_process) -> str:
    """
    Takes in 'string_to_process' from an input and
    returns 5 marijuana strain recommendations.

    Args:
        string_to_process ([str]): [string input]

    Returns:
        List of Dictionaries containing strain
        recommendations
    """
    # modeling happens here
    rec = string_to_process.upper()
    return {"Recommendations": {rec}}
