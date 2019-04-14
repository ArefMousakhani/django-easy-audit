import pymongo


class MongoConnection(object):
    def __init__(self, address, db_name):
        self.address = address
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            if self.connection is not None:
                self.connection.close()
            self.connection = pymongo.MongoClient(self.address, serverSelectionTimeoutMS=2)
        except:
            pass

    def insert(self, collection_name, data):
        try:
            collection = getattr(getattr(self.connection, self.db_name), collection_name)
            collection.insert(data)

        except:
            if self.connection is not None:
                self.connection.close()
            self.connect()
            raise ConnectionError
