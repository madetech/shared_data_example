from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from os import environ as env

app = FastAPI()

templates = Jinja2Templates(directory="templates")

name = "John Doe"

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "FastAPI - page 1", "name": f"{name}"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)