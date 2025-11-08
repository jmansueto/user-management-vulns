from flask import Blueprint, request, jsonify
import models
import auth

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400
    
    hashed_password = auth.hash_password(password)
    
    try:
        user_id = models.create_user(username, email, hashed_password)
        token = auth.generate_jwt(user_id, username)
        return jsonify({'message': 'User created successfully', 'user_id': user_id, 'token': token}), 201
    except:
        return jsonify({'error': 'User already exists'}), 400

@users_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = models.get_user_by_username(username)
    
    if user and auth.verify_password(password, user['password']):
        token = auth.generate_jwt(user['id'], user['username'])
        return jsonify({'message': 'Login successful', 'token': token})
    
    return jsonify({'error': 'Invalid credentials'}), 401

@users_bp.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = models.get_user_by_id(user_id)
    
    if user:
        return jsonify({
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'bio': user['bio']
        })
    
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/api/users/search', methods=['GET'])
def search_users():
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({'error': 'Search query required'}), 400
    
    users = models.search_users(query)
    
    results = []
    for user in users:
        results.append({
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'bio': user['bio']
        })
    
    return jsonify({'query': query, 'results': results})

@users_bp.route('/api/password/reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')
    
    token = auth.generate_reset_token()
    
    from utils import send_password_reset_email
    send_password_reset_email(email, token)
    
    return jsonify({'message': 'Password reset email sent', 'token': token})

