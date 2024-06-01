from fastapi import APIRouter
from pydantic import BaseModel
from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

class UserIn(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserIn):
    return auth_service.register(user)

@router.post("/login")
def login(user: UserIn):
    return auth_service.login(user)
