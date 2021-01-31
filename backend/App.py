from flask import Flask, request, send_file, redirect, url_for
import flask
from werkzeug.utils import secure_filename
from Services import GameService, PlayerService
import os
from chessGame import chessGame
from player import Player

UPLOAD_FOLDER = 'uploads'


app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'howdy cowboy'


@app.route('/')
def frontend():
    return app.send_static_file('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def playerDashboard():
    content = request.json
    print(content)
    email = content['email']

    foundPlayer = PlayerService.read_player(email)

    if foundPlayer is None:
        newPlayer = Player(email, email)
        PlayerService.add_player(newPlayer)
        return {"Success": True, "Message": "Created new player", "Player": newPlayer, "OpenGames": []}

    allGames = GameService.read_all_open_games_for_player(foundPlayer.email)

    return {"Success": True, "Message": "Found player", "Player": foundPlayer, "OpenGames": allGames}


@app.route('/dashboard/changename', methods=['GET', 'POST'])
def changeName():
    content = request.json
    print(content)
    name = content['name']
    email = content['email']

    foundPlayer = PlayerService.read_player(email)

    if foundPlayer is None:
        return {"Success": False, "Message": "Failed to find player", "Player": None, "OpenGames": []}

    foundPlayer.screenName = name
    PlayerService.update_player(email, foundPlayer)

    return {"Success": True, "Message": "Updated Name", "Player": foundPlayer}


@app.route('/game/create', methods=['GET', 'POST'])
def createGame():
    content = request.json
    print(content)
    # REMOVE
    email = content['email']
    color = content['color']
    size = content['size']

    newGame = chessGame(email, color, size)

    success, message = GameService.create_new_game(newGame)

    return {"success": success, "message": message, "gameID": newGame.gameID}


@app.route('/game/join', methods=['GET', 'POST'])
def joinGame():
    content = request.json
    print(content)
    email = content['email']
    gameID = content['gameID']

    foundGame = GameService.get_game_by_id(gameID)

    if foundGame is None:
        return {"Success": False, "Message": "Could not find game"}

    if not foundGame.playerJoin(email):
        return {"Success": False, "Message": "Could not join game"}

    success, message = GameService.update_game(gameID, foundGame)

    return {"Success": success, "Message": message}


@app.route('/game/makemove', methods=['GET', 'POST'])
def makeMove():
    content = request.json
    print(content)
    gameID = content['gameID']
    email = content['email']
    pieceID = content['pieceID']
    location = content['location']

    foundGame = GameService.get_game_by_id(gameID)


    if foundGame is None:
        return {"Success": False, "Message": "Could not find game"}

    out = foundGame.makeMove(email, pieceID, location)

    return {"Success": out[0], "Message": out[1]}


@app.route('/game/resign', methods=['GET', 'POST'])
def resign():
    content = request.json
    print(content)
    gameID = content['gameID']
    email = content['email']

    foundGame = GameService.get_game_by_id(gameID)

    if foundGame is None:
        return {"Success": False, "Message": "Could not find game"}

    if foundGame.playerResign(email):
        return {"Success": True, "Message": "Player Resigned"}

    return {"Success": False, "Message": "Could not resign game"}


@app.route('/game/currentstate', methods=['GET', 'POST'])
def getGameBoardState():
    content = request.json
    print(content)
    gameID = content['gameID']
    email = content['email']

    foundGame = GameService.get_game_by_id(gameID)
    if foundGame is None:
        return {"Success": False, "Message": "Could not find game"}

    out = foundGame.getGameBoard(email)
    if out == -1:
        return {"Success": False, "Message": "Could not find player"}

    return {
        "Success": True, "Message": "Got Board State",
        "Board": out[0],
        "Size": out[1],
        "Turn": out[2],
        "Player": out[3]
    }


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
