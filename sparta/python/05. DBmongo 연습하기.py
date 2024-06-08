from pymongo import MongoClient
client = MongoClient('mongodb+srv://sayya:sparta@cluster0.regsz.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name' : 'bob',
    'age' : 27
}

db.users.insert_one(doc)