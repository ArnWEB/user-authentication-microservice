from app.models.user import User
from app.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register(self, user_data):
        # Logic to register a user
        user = User(username=user_data.username, password=user_data.password)
        return self.user_repo.create(user)

    def login(self, user_data):
        # Logic to authenticate user
        user = self.user_repo.get_by_username(user_data.username)
        if user and user.password == user_data.password:
            return {"message": "Login successful"}
        else:
            return {"message": "Invalid credentials"}
