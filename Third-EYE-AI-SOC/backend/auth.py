from jose import jwt
from datetime import datetime, timedelta

SECRET = "third_eye_secret"

def create_token(user):
    payload = {
        "user": user,
        "exp": datetime.utcnow() + timedelta(hours=5)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
