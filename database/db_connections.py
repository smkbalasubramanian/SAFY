import pymongo
from pymongo import *
from config.config import MONGO_DB_CLIENT,MONGO_DB_NAME,MONGO_DB_COLLECTION
import pymysql
def mongo_db_connection():
    myclient = pymongo.MongoClient(MONGO_DB_CLIENT)
    safy_db = myclient[MONGO_DB_NAME]
    safy_conctn = safy_db[MONGO_DB_COLLECTION]
    collection = safy_db.get_collection(MONGO_DB_COLLECTION)
    return safy_conctn


def sql_connecion():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='youtube_db1'
    )
    cursor = conn.cursor()
    return [cursor,conn]