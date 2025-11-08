import bcrypt
import random
import json
import base64
from config import Config

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def generate_reset_token():
    token = random.randint(100000, 999999)
    return str(token)

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

