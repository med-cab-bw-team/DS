"""This file is for database managment"""
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
# from pydantic import BaseModel  <-- To be used for database schema set up


class DataBase:
    """Creates a Data Base object"""

    load_dotenv()

    def connect_mongodb_client(self):
        """Connect to MongoDB client"""
        MongoUSER = getenv('MongoUSER', default="OOPS")
        MongoPASS = getenv('MongoPASS', default="OOPS")
        MongoNAME = getenv('MongoNAME', default="OOPS")
        client = MongoClient(
            f"mongodb+srv://{MongoUSER}:{MongoPASS}@{MongoNAME}?\
                retryWrites=true&w=majority"
        )

        return client
