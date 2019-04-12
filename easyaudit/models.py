import datetime
from easyaudit.connection import MongoConnection
import logging

from easyaudit.settings import (
    MONGODB_REQUEST_COLLECTION_NAME,
    MONGODB_LOGIN_COLLECTION_NAME,
    MONGODB_CRUD_COLLECTION_NAME,
    MONGODB_ADDRESS,
    MONGODB_NAME
)

mongo_connection = MongoConnection(MONGODB_ADDRESS, MONGODB_NAME)
mongo_connection.connect()

logging.basicConfig(filename='logging.log', filemode='a', format='%(message)s')


class BaseMongoModel(object):

    @staticmethod
    def insert(collection_name, **kwargs):
        if 'datetime' not in kwargs:
            kwargs['datetime'] = str(datetime.datetime.now())

        try:
            mongo_connection.insert(collection_name, kwargs)

        except ConnectionError:
            logging.warning('mongo-db-connection-error - %s' % (
                kwargs
            ))


class CRUDEvent(BaseMongoModel):
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    M2M_CHANGE = 4
    M2M_CHANGE_REV = 5

    def __init__(self):
        super().__init__()

    def save(self, **kwargs):
        self.insert(MONGODB_CRUD_COLLECTION_NAME, **kwargs)


class LoginEvent(BaseMongoModel):
    LOGIN = 0
    LOGOUT = 1
    FAILED = 2

    def __init__(self):
        super().__init__()

    def save(self, **kwargs):
        self.insert(MONGODB_LOGIN_COLLECTION_NAME, **kwargs)


class RequestEvent(BaseMongoModel):
    def __init__(self):
        super().__init__()

    def save(self, **kwargs):
        self.insert(MONGODB_REQUEST_COLLECTION_NAME, **kwargs)
