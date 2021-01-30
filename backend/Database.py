import pymongo


client = pymongo.MongoClient(
   "mongodb+srv://db-user:WECChamps-2021!@wec-2021.rur9n.mongodb.net/WEC-2021?retryWrites=true&w=majority")
db = client['WEC2021']
collection = db['TestCollection']


def read(stuff):
    pass


def read_all():
    for item in collection.find():
        print(item)


def insert_user(username):
    collection.insert_one({'username': username})
