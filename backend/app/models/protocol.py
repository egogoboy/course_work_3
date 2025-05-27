from typing import Protocol

class HasIDAndUsername(Protocol):
    id: int
    username: str

def print_user_info(user: HasIDAndUsername):
    print(f"User ID: {user.id}, Username: {user.username}")
