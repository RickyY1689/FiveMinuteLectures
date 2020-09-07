from flask import Flask

UPLOAD_FOLDER = './audiofiles'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    from .views import main 
    print("hello")
    app.register_blueprint(main)
    return app