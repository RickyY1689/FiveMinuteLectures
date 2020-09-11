from flask import Flask
from flask_cors import CORS, cross_origin


UPLOAD_FOLDER = './audiofiles'

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = "658d7edc37cd8c1b37c0da46"
    from .views import main 
    app.register_blueprint(main)
    return app