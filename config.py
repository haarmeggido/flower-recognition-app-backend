import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# General settings
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
DATABASE = "instance/users.db"
TOKEN_EXPIRATION_HOURS = 24

#test