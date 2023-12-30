from pymongo import MongoClient


def get_database():
    CONNECTION_STR = "mongodb://localhost:27017/"

    # Connect to MongoDB database
    client = MongoClient(CONNECTION_STR)

    # Return database
    return client["task_tracker_db"]


def get_collection():
    db = get_database()

    return db["tasks"]
