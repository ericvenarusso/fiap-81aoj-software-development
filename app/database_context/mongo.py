import os
from pymongo import MongoClient


class MongoContext:
    def __init__(self, database):
        client = MongoClient(os.getenv("MONGODB_URL", "localhost:27017"))
        self.db = client[database] 

    def insert(self, collection, object):
        self.db[collection].insert_one(object)

    def insert_many(self, collection, object):
        self.db[collection].insert_many(object)

    def select(self, collection, filter=None):
        if filter is None:
            return self.db[collection].find()
        else:
            return self.db[collection].find(filter)

    def select_fields(self, collection, filter, projection):
        return self.db[collection].find(filter, projection)

    def update(self, collection, filter, new_value):
        self.db[collection].update_one(filter, new_value)

    def update_many(self, collection, filter, new_value):
        self.db[collection].update_many(filter, new_value)
