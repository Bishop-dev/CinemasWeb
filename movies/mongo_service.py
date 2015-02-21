import time
import datetime
import pymongo
from cinemas_web.settings import MONGODB


class MongoService():
    LIMIT = 40

    def __init__(self):
        time_pattern = time.strftime('%d_%m_%y')
        connection = pymongo.Connection(MONGODB['HOST'], MONGODB['PORT'])
        self.db = connection[MONGODB['DB']]
        self.daily = self.db[MONGODB['MONGODB_COLLECTION_DAILY'] + time_pattern]
        self.active = self.db[MONGODB['MONGODB_COLLECTION_ACTIVE'] + time_pattern]

    def fetch_all(self):
        return self.daily.find().sort('session', pymongo.ASCENDING)

    def fetch_default_limit(self):
        return self.fetch_limit(self.LIMIT)

    def fetch_limit(self, limit):
        return self.daily.find({'session': {'$gt': datetime.datetime.now()}}).limit(limit)

    def fetch_page(self, _id):
        return self.daily.find({'_id': {'$gt': _id}, 'session': {'$gt': datetime.datetime.now()}}).limit(self.LIMIT)