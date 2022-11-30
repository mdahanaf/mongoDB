import pymongo
import requests

# database creation and connection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["ahanaf"]
collection = db["user_data"]

u = input("Username: ")
p = input("Password: ")
e = input("E-mail: ")

collection.insert_one({"user": u, "pass": p, "email": e})


