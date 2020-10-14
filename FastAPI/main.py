from fastapi import FastAPI

api = FastAPI()


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
