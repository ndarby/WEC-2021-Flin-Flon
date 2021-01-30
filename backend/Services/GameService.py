import pymongo


client = pymongo.MongoClient(
   "mongodb+srv://db-user:WECChamps-2021!@wec-2021.rur9n.mongodb.net/WEC-2021?retryWrites=true&w=majority")
db = client['WEC2021']

gameCollection = db['Games']


def read_all_games():
    for item in gameCollection.find():
        print(item)


def read_all_open_games_for_player(email):
    games = []
    query = {"$or": [{"blackPlayer": email, "completed": False}, {"whitePlayer": email, "completed": False}]}
    for item in gameCollection.find(query):
        games.append(item)
    return games


def get_game_by_id(gameID):
    query = {"gameID": gameID}
    game = gameCollection.find_one(query)
    return game


def check_game_id_unused(gameID):
    if gameCollection.find({"gameID": gameID}).count() != 0:
        return True
    return False


def create_new_game(game):
    gameCollection.insert_one(game)
    return True, "Game Created Successfully"


def update_game(gameID, game):
    gameCollection.update_one({"gameID": gameID}, game, upsert=False)
    return True, "Game Updated Successfully"

def get_chess_board_for_game(gameID):
    game = get_game_by_id(gameID)
    if game is not None:
        return game.board

    return None


def update_chess_board(gameID, board):
    gameCollection.update_one({"gameID": gameID}, {'$set': {"board": board}}, upsert=False)

