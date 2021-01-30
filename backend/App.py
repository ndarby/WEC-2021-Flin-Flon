from flask import Flask, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
import os

from backend.Services import PlayerService

UPLOAD_FOLDER = 'uploads'


app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'howdy cowboy'


def check_username(name):
    return name == 'moose'


@app.route('/')
def frontend():
    return app.send_static_file('index.html')


@app.route('/requests', methods=['GET', 'POST'])
def requests():
    print(f'method: {request.method}')
    print('---form data fields---')
    for key, value in request.form.items():
        print(f'{key}: {value}')

    return {'gameID': request.form['gameID']}



@app.route('/upload_request', methods=['POST'])
def upload():
    try:
        file = request.files['file']
    except KeyError:
        return {'message': 'no file found'}
    filename = secure_filename(file.filename)
    if not filename:
        return {'message': 'no filename given'}
    destination = os.path.join(UPLOAD_FOLDER, filename)
    file.save(destination)
    return {'message': 'file uploaded successfully'}


@app.route('/download_request', methods=['POST', 'GET'])
def download():
    filename = os.listdir('uploads')[0]
    return send_file(os.path.join('uploads', filename), attachment_filename=filename)


@app.errorhandler(404)
def error404(e):
    return redirect(url_for('frontend'))


if __name__ == '__main__':
    app.run()
