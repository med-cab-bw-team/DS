from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv


class DataBase:
    """Creates a Data Base object"""

    load_dotenv()

    def connect_mongodb_client(self):
        """Connect to MongoDB client"""
        MongoUSER = getenv('MongoUSER', default="OOPS")
        MongoPASS = getenv('MongoPASS', default="OOPS")
        MongoNAME = getenv('MongoHOST', default="OOPS")
        client = MongoClient(
            f"mongodb+srv://{MongoUSER}:{MongoPASS}@{MongoNAME}?\
                retryWrites=true&w=majority"
        )

        return client
