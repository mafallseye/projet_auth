from http import client
from uuid import uuid4
import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['Users']
info=mydb.userinfo

User={
    "userid":"1",
    "mail":"maxe@gmail.com",
    "username":"maxe",
    "password":"123456789"
}
info.insert_one(User)