class Repository:
    def __init__(self, database_context):
        self.database_context = database_context

    def insert(self, collection, object):
        self.database_context.insert(collection, object)

    def insert_many(self, collection, object):
        self.database_context.insert_many(collection, object)

    def select(self, collection, filter=None):
        return self.database_context.select(collection, filter=filter)

    def select_fields(self, collection, filter, projection):
        return self.database_context.select_fields(collection, filter, projection)

    def update(self, collection, filter, new_value):
        self.database_context.update(collection, filter, new_value)

    def update_many(self, collection, filter, new_value):
        self.database_context.update_many(collection, filter, new_value)
