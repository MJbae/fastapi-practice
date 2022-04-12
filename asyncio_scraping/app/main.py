from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.models import mongodb

BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이"},
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, s: str):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "practice fastapi"}
    )


@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    """after app shutdown"""
    mongodb.close()
