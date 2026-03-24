from jose import jwt
SECRET="secret"
def create_token(data): return jwt.encode(data, SECRET, algorithm="HS256")
def verify_token(t): return jwt.decode(t, SECRET, algorithms=["HS256"])