from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect_to_mongodb():
    try:
        client = MongoClient("mongodb+srv://User:user@mongodb1.dz8ee6z.mongodb.net/hangman_game_db")
        db = client.hangman_game_db
        print("|-----> DB RUNNING <-----|")
    except ConnectionFailure as e:
        print("Error de Conexion", e)
    return db

""" Function to connect to mongodb """
def get_mongodb_client():
    return connect_to_mongodb()
