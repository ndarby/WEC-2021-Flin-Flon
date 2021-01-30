import pymongo


client = pymongo.MongoClient(
   "mongodb+srv://db-user:WECChamps-2021!@wec-2021.rur9n.mongodb.net/WEC-2021?retryWrites=true&w=majority")
db = client['WEC2021']

playerCollection = db['Players']


def read_player(email):
    player = playerCollection.find_one({"email": email})
    return player


def update_player(email, player):
    playerCollection.find_one_and_replace({"email": email}, player)
    return True, f"Player with email {email} was updated successfully"






