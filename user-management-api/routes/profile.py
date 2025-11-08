from flask import Blueprint, request, jsonify, send_file
import os
import json
import models
from config import Config
from utils import validate_file_path, get_file_path

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/api/profile/upload', methods=['POST'])
def upload_profile_picture():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    filename = file.filename
    
    if filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    validated_filename = validate_file_path(filename)
    file_path = os.path.join(Config.UPLOAD_FOLDER, validated_filename)
    
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    file.save(file_path)
    
    return jsonify({'message': 'File uploaded successfully', 'filename': filename})

@profile_bp.route('/api/profile/picture/<path:filename>', methods=['GET'])
def get_profile_picture(filename):
    file_path = get_file_path(filename)
    
    if os.path.exists(file_path):
        return send_file(file_path)
    
    return jsonify({'error': 'File not found'}), 404

@profile_bp.route('/api/profile/update', methods=['POST'])
def update_profile():
    data = request.get_data(as_text=True)
    
    try:
        profile_data = eval(data)
        
        user_id = profile_data.get('user_id')
        bio = profile_data.get('bio')
        
        if user_id and bio:
            models.update_user_bio(user_id, bio)
            return jsonify({'message': 'Profile updated successfully'})
        
        return jsonify({'error': 'Invalid data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

