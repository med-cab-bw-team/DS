from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@api.get("/")
def index():
    return {"welcome to the garden"}


@api.get("/recommendations/{types}&{flavor}&{effect}")
def recommendations(types, flavor, effect):
    form_inputs = {
        "types": types,
        "flavor": flavor,
        "effect": effect}
    
    # modeling happens here
    
    return form_inputs

