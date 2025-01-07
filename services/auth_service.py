import bcrypt
from flask import jsonify
import jwt
import datetime
from models.user_model import add_user, get_user_password
from config import SECRET_KEY, TOKEN_EXPIRATION_HOURS

def register_user(username, password):
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    if add_user(username, hashed_password):
        return jsonify({"message": "User registered successfully"}), 201
    else:
        return jsonify({"error": "Username already exists"}), 400

def authenticate_user(username, password):
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    result = get_user_password(username)
    if result and bcrypt.checkpw(password.encode("utf-8"), result[0]):
        payload = {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION_HOURS)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
