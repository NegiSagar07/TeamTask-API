from fastapi import FastAPI
from app.db import engine
from sqlalchemy import text


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    print("async database connected successfully")


@app.get("/")
def hello():
    return {"hello" : "bro"}