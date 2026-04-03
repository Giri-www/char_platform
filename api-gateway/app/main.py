from fastapi import FastAPI
from app.routers import auth_routers, user_routers, chat_routers

app = FastAPI()

app.include_router(auth_routers.router)
# app.include_router(user_routers.router)
# app.include_router(chat_routers.router)


@app.get("/")
def home():
    return {"message": "API Gateway Running"}