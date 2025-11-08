from flask import Blueprint, request, jsonify, send_file
import os
import json
import models
from config import Config
from werkzeug.utils import secure_filename

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/api/profile/upload', methods=['POST'])
def upload_profile_picture():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    filename = file.filename
    
    if filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    safe_filename = secure_filename(filename)
    file_path = os.path.join(Config.UPLOAD_FOLDER, safe_filename)
    
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    file.save(file_path)
    
    return jsonify({'message': 'File uploaded successfully', 'filename': safe_filename})

@profile_bp.route('/api/profile/update', methods=['POST'])
def update_profile():
    try:
        profile_data = request.get_json()
        
        user_id = profile_data.get('user_id')
        bio = profile_data.get('bio')
        
        if user_id and bio:
            models.update_user_bio(user_id, bio)
            return jsonify({'message': 'Profile updated successfully'})
        
        return jsonify({'error': 'Invalid data'}), 400
    except Exception:
        return jsonify({'error': 'Failed to update profile'}), 400

