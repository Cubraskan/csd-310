from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ihluj.mongodb.net/pytech"
client=MongoClient(url)
db=client.pytech
print("--Pytech Collection List--\n", (db.list_collection_names()))
input("Program has finished, please press Enter to exit...")