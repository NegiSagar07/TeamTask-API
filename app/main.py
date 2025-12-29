from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.auth import router as auth_router
from app.routes.task import router as task_router


app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(task_router)

@app.get("/home")
async def health():
    return {"status": "ok"}
