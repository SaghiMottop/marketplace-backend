from fastapi import FastAPI
from db import models

from db.database import engine

app = FastAPI()



@app.get("/hello")
def index():
    return "Hello Team 1"

models.Base.metadata.create_all(engine)