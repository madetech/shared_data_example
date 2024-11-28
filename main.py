from fastapi import FastAPI
from os import environ as env
app = FastAPI()

@app.get("/")
def index():
  return {"message": f"Secret: {env['SECRET_IDENTITY']}"}