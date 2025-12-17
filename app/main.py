from fastapi import FastAPI
from app.db import get_db_connection


app = FastAPI()


@app.on_event("startup")
def startup_event():
    conn = get_db_connection()
    conn.close()
    print("Database connected successfully")


@app.get("/")
def hello():
    return {"hello" : "bro"}