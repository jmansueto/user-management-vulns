import os

class Config:
    SECRET_KEY = "flask-secret-key-12345"
    JWT_SECRET = "jwt-super-secret-key-67890"
    DATABASE_PATH = "users.db"
    UPLOAD_FOLDER = "./uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_USERNAME = "noreply@example.com"
    SMTP_PASSWORD = "email-password-123"

