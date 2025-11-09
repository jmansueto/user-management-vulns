from flask import Flask
from config import Config
import models
from routes.users import users_bp
from routes.profile import profile_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(users_bp)
app.register_blueprint(profile_bp)

@app.route('/')
def index():
    return {'message': 'User Management API', 'version': '1.0.0'}

if __name__ == '__main__':
    models.init_db()
    app.run(debug=False, host='0.0.0.0', port=5000)

