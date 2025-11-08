# User Management API

⚠️ **WARNING: This repository contains known security vulnerabilities and is intended for demonstration and testing purposes only. DO NOT use this code in production environments.**

A simple Flask-based user management API with registration, authentication, and profile management features.

## Features

- User registration and login
- JWT-based authentication
- User search functionality
- Profile picture uploads
- Profile management
- Password reset via email

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Authentication
- `POST /api/register` - Register a new user
  ```json
  {
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
  }
  ```

- `POST /api/login` - Login with username and password
  ```json
  {
    "username": "john",
    "password": "password123"
  }
  ```

### Users
- `GET /api/users/<id>` - Get user by ID
- `GET /api/users/search?q=<query>` - Search users by username or email

### Profile
- `POST /api/profile/upload` - Upload profile picture (multipart/form-data)
- `GET /api/profile/picture/<filename>` - Get profile picture
- `POST /api/profile/update` - Update user profile
  ```json
  {
    "user_id": 1,
    "bio": "Software developer"
  }
  ```

### Password Reset
- `POST /api/password/reset` - Request password reset
  ```json
  {
    "email": "john@example.com"
  }
  ```

## Tech Stack

- Python 3.x
- Flask 3.0.0
- SQLite

