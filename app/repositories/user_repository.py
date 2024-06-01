from app.models.user import User

class UserRepository:
    def create(self, user: User):
        # Logic to save user data to database
        return {"message": "User created successfully"}

    def get_by_username(self, username: str):
        # Logic to retrieve user from database
        # This is just a placeholder, replace with actual DB query
        return User(username=username, password="hashedpassword")
