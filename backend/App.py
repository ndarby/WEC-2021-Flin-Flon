from flask import Flask, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'


app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'howdy cowboy'


@app.route('/')
def frontend():
    return app.send_static_file('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def playerDashboard(email):
    pass


@app.route('/game/create', methods=['GET', 'POST'])
def createGame(email, color, size):
    pass


@app.route('game/join', methods=['GET', 'POST'])
def joinGame(email, gameID):
    pass


@app.route('game/makemove', methods=['GET', 'POST'])
def makeMove(gameID, email, pieceID, location):
    pass


@app.route('game/resign', methods=['GET', 'POST'])
def resign(gameID, email):
    pass


@app.route('game/currentstate', methods=['GET', 'POST'])
def getGameBoardState(gameID,email):
    pass


@app.route('/requests', methods=['GET', 'POST'])
def requests():
    print(f'method: {request.method}')
    print('---form data fields---')
    for key, value in request.form.items():
        print(f'{key}: {value}')
    #PlayerService.insert_user(request.form['username'])
    return {'message': 'hello moose',
            'username': request.form['username']}


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
