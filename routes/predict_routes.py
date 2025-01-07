from flask import Blueprint, request, jsonify
from services.prediction_service import predict_image

predict_blueprint = Blueprint("predict", __name__)

@predict_blueprint.route("/", methods=["POST"])
def predict():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    return predict_image(file)
