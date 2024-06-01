from fastapi import FastAPI
from app.controllers import auth_controller,health_controller

app = FastAPI()

app.include_router(auth_controller.router)
app.include_router(health_controller.router)
