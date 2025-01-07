import jwt
from flask import request, jsonify
from config import SECRET_KEY

def decode_jwt():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None, {"error": "Missing Authorization header"}, 401

    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload, None
    except jwt.ExpiredSignatureError:
        return None, {"error": "Token has expired"}, 401
    except jwt.InvalidTokenError:
        return None, {"error": "Invalid token"}, 401
