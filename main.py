# Routes for user actions (register, login, update)
import os
import uvicorn
from fastapi import FastAPI
from auth import authentication
from db import models
from routers import user, ads, category, file
from db.database import engine
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(user.router)

app.include_router(ads.router)
app.include_router(category.router)
app.include_router(authentication.router)
app.include_router(file.router)



@app.get("/")
def index():
    return {"status": "ok"}



models.Base.metadata.create_all(engine)


app.mount('/files', StaticFiles(directory="files"), name='files')



if __name__ == "__main__":
    # Important: disable reload while debugging
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="debug",
    )
