from flask import Flask
from flask_cors import CORS
from src.main.routes import api_route_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_route_bp)
