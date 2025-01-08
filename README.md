# Flower Recognition WebApp Backend

This is the backend for a Flower Recognition WebApp built with Flask. The webapp allows users to register, log in, upload images, and get flower predictions using a trained machine learning model (ResNet-152).

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the App](#running-the-app)
- [API Endpoints](#api-endpoints)
  - [Auth Routes](#auth-routes)
  - [Prediction Routes](#prediction-routes)
  - [User Routes](#user-routes)
- [Model Details](#model-details)
- [License](#license)

---

## Overview

The backend for the flower recognition webapp is developed using Flask and provides several features such as user authentication, flower image prediction, and user details management.

### Key Features:
- **User Authentication**: Register and log in users using JWT tokens.
- **Image Prediction**: Predict flower species from uploaded images using a pre-trained ResNet-152 model.
- **User Management**: Users can view and update their details, including email and flower recognition statistics.

---

## Project Structure

The project is organized as follows:

```
flower-recognition-app-backend/
│
├── instance/
│   └── users.db              # SQLite database storing user data
│
├── models/
│   ├── database.py           # Database initialization and connections
│   └── user_model.py         # User-related database operations
│
├── routes/
│   ├── auth_routes.py        # Authentication-related routes (login, register)
│   ├── predict_routes.py     # Prediction route for flower images
│   └── user_routes.py        # User profile-related routes (update, get user details)
│
├── services/
│   ├── auth_service.py       # Logic for registering and authenticating users
│   └── prediction_service.py # Logic for flower image prediction
│
├── utils_app/
│   └── jwt_utils.py          # JWT token utilities for decoding tokens
│
├── .env                      # Environment variables
├── .gitignore                # Git ignore file
├── app.py                    # Main entry point of the app
├── config.py                 # Configuration settings
├── requirements.txt          # Required Python packages
└── trained_model.pth         # Pre-trained ResNet-152 model
```

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flower-recognition-app-backend.git
   cd flower-recognition-app-backend
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy `.env.example` to `.env` and set the appropriate values for `SECRET_KEY`.

5. Initialize the database:
   ```bash
   python app.py
   ```

---

## Configuration

The configuration for the backend app is located in the `config.py` file. You need to set up your `SECRET_KEY` and ensure the correct path for your database (`instance/users.db`).

To customize the configuration, you can create a `.env` file in the root of the project directory with the following environment variables:

```env
SECRET_KEY=your_secret_key
```

---

## Running the App

To run the app locally in development mode:

```bash
python app.py
```

For production mode, you can use a WSGI server like `waitress` (uncomment the `serve` line in `app.py`).

```bash
# Install waitress
pip install waitress

# Run the app with waitress
python app.py
```

The app will run on `http://0.0.0.0:8080`.

---

## API Endpoints

### Auth Routes

- **POST /auth/register**
  - Registers a new user.
  - Payload: `{ "username": "string", "password": "string" }`
  - Response: `{ "message": "User registered successfully" }` or `{ "error": "Username already exists" }`

- **POST /auth/login**
  - Logs in a user and returns a JWT token.
  - Payload: `{ "username": "string", "password": "string" }`
  - Response: `{ "message": "Login successful", "token": "jwt_token" }` or `{ "error": "Invalid credentials" }`

### Prediction Routes

- **POST /predict**
  - Predicts the flower species from an uploaded image.
  - Payload: `{ "file": "image" }`
  - Response: `{ "predicted_label": "flower_name", "predicted_class": 0 }` or `{ "error": "Error during prediction" }`

### User Routes

- **POST /user/update**
  - Updates user details (email, recognitions, flower mask).
  - Payload: `{ "email": "string", "total_recognitions": "int", "unique_recognitions": "int", "flower_mask": "int" }`
  - Response: `{ "message": "User updated successfully" }` or `{ "error": "Invalid data format" }`

- **GET /user/get**
  - Fetches user details.
  - Response: `{ "username": "string", "email": "string", "total_recognitions": "int", "unique_recognitions": "int", "flower_mask": "int" }` or `{ "error": "User not found" }`

---

## Model Details

The model used for flower prediction is **ResNet-152**, trained on 3000 images of 26 different flower species. It is fine-tuned for classifying flower types and is stored in the file `trained_model.pth`.

The model takes in an image, preprocesses it, and outputs one of the 26 flower species labels.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes

- Ensure the server has enough memory and GPU (if available) for running the model, as it uses PyTorch for inference.
- The app uses Flask and SQLite, so the app can be easily deployed on lightweight platforms such as Heroku or a similar environment.


---
### Temporary - photos of ML process

![obraz](https://github.com/user-attachments/assets/67e2541b-6dba-4088-bee4-74c110afc1d7)
![obraz](https://github.com/user-attachments/assets/d07e1968-fd57-4d38-b0df-d60305480a27)
![obraz](https://github.com/user-attachments/assets/11912310-44b5-477b-9e91-1783005989e9)
![obraz](https://github.com/user-attachments/assets/7132cb86-381f-43f3-ac5b-7cb0c1f61c1c)


