from pymongo import MongoClient
import os
from dotenv import load_dotenv

#load enviroment variables
load_dotenv ()

#connect to mongo atlas cluster
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

#Access/ choose database namew

db = client["todo_api"]  

#pick a collection to operate on inside that database
todo_collection = db["todo"]