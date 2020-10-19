from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def mount_static_directory(api):
    api.mount(
        "/static",
        StaticFiles(directory="FastAPI/static"),
        name="static")


templates = Jinja2Templates(
    directory="FastAPI/templates"
    )