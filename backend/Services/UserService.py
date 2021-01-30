import pymongo


client = pymongo.MongoClient(
   "mongodb+srv://db-user:WECChamps-2021!@wec-2021.rur9n.mongodb.net/WEC-2021?retryWrites=true&w=majority")
db = client['WEC2021']

userCollection = db['Users']


def insert_user(username, password):
    if userCollection.find({'username': username}).count() > 0:
        return False, f"User with username {username} already exists"

    userCollection.insert_one({'username': username, "password": password})
    return True, f"User with username {username} was created successfully"


def login_user(username, password):
    user = userCollection.find_one({'username': username})
    if user.count() > 0:
        if user.password == password:
            return True, f"{username} successfully logged in"

    return False, f"Username or password is incorrect"





