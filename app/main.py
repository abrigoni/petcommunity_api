from fastapi import FastAPI
from .api.v1.api import api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix='/v1')
