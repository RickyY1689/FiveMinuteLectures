from flask import Blueprint, flash, jsonify, request, redirect, url_for, send_from_directory
from flask import current_app as app
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './audiofiles'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'pdf'}
main = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/test', methods=['POST'])
def add_test():
    return "AHAHAHA SUCCESS BAYBEEEEEE", 201 

@main.route('/upload-file', methods=['POST'])
@cross_origin()
def upload_file():
    name=""
    basedir = os.path.abspath(os.path.dirname(__file__))
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "MonkaS"
        file = request.files['file']
        name=file.filename
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))
            return name, 201
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)