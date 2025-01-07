from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_blueprint
from routes.predict_routes import predict_blueprint
from routes.user_routes import user_blueprint
from models.database import init_db



# Initialize Flask app
app = Flask(__name__)
CORS(app)

CORS(auth_blueprint, supports_credentials=True)
CORS(predict_blueprint, supports_credentials=True)
CORS(user_blueprint, supports_credentials=True)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(predict_blueprint, url_prefix="/predict")
app.register_blueprint(user_blueprint, url_prefix="/user")

init_db()


if __name__ == "__main__":
    # Development mode
    app.run(host="0.0.0.0", port=8080)

    # Production mode
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
