import pymongo
from pymongo import *
from youtube_harvesting.config.config import  MONGO_DB_CLIENT,MONGO_DB_NAME,MONGO_DB_COLLECTION

def mongo_db_connection():
    myclient = pymongo.MongoClient(MONGO_DB_CLIENT)
    safy_db = myclient[MONGO_DB_NAME]
    safy_conctn = safy_db[MONGO_DB_COLLECTION]
    collection = safy_db.get_collection(MONGO_DB_COLLECTION)
    print("connection created")
    print(myclient.list_database_names())
    return collection