from flask import Blueprint, request, jsonify
from models.user_model import update_user, get_user_by_username
from utils_app.jwt_utils import decode_jwt
from models.user_model import get_user_full

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/update", methods=["POST"])
def update_user_details():
    payload, error_response = decode_jwt()
    if error_response:
        return jsonify(error_response), 401

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Invalid token"}), 401

    data = request.get_json()

    # Fetch current user details from the database
    user = get_user_by_username(username)  
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Merge current user details with incoming data
    email = data.get("email", user["email"])
    total_recognitions = data.get("total_recognitions", user["total_recognitions"])
    unique_recognitions = data.get("unique_recognitions", user["unique_recognitions"])
    flower_mask = data.get("flower_mask", user["flower_mask"])

    # Validate numeric fields
    if not all(isinstance(x, (int, type(None))) for x in [total_recognitions, unique_recognitions, flower_mask]):
        return jsonify({"error": "Invalid data format"}), 400

    # Update the user in the database
    update_user(username, email, total_recognitions, unique_recognitions, flower_mask)
    return jsonify({"message": "User updated successfully"}), 200

@user_blueprint.route("/get", methods=["GET"])
def get_user_details():
    payload, error_response = decode_jwt()
    if error_response:
        return jsonify(error_response), 401

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Invalid token"}), 401

    user = get_user_full(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200
