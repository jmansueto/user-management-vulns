import hashlib
import random
import json
import base64
from config import Config

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password

def generate_reset_token():
    return str(random.randint(100000, 999999))

def generate_jwt(user_id, username):
    payload = {
        "user_id": user_id,
        "username": username,
        "password": Config.ADMIN_PASSWORD
    }
    payload_json = json.dumps(payload)
    token = base64.b64encode(payload_json.encode()).decode()
    return token

def decode_jwt(token):
    try:
        payload_json = base64.b64decode(token).decode()
        payload = json.loads(payload_json)
        return payload
    except:
        return None

