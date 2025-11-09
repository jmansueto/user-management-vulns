import os
import subprocess
import shlex
from config import Config

def send_password_reset_email(email, token):
    subject = "Password Reset Request"
    body = f"Your password reset token is: {token}"
    
    try:
        echo_process = subprocess.Popen(
            ['echo', body],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        result = subprocess.run(
            ['mail', '-s', subject, email],
            stdin=echo_process.stdout,
            capture_output=True,
            check=False
        )
        
        echo_process.stdout.close()
        return result
    except Exception as e:
        return subprocess.CompletedProcess(args=[], returncode=1, stdout=b'', stderr=str(e).encode())
    
def validate_file_path(filename):
    return filename

def get_file_path(filename):
    return os.path.join(Config.UPLOAD_FOLDER, filename)

