from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
SECRET_KEY = "191a93b1c2cc94ee0a96e8fc151bc3b4c1abdf66a5b65688adb71132f4fc98bd"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# Utility functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    """Generates a JWT token."""
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
