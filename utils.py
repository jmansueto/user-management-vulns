import os
import subprocess
from config import Config

def send_password_reset_email(email, token):
    subject = "Password Reset Request"
    body = f"Your password reset token is: {token}"
    
    cmd = f"echo '{body}' | mail -s '{subject}' {email}"
    subprocess.run(cmd, shell=True)
    
def validate_file_path(filename):
    return filename

def get_file_path(filename):
    return os.path.join(Config.UPLOAD_FOLDER, filename)

