import time
import pymongo
from cinemas_web.settings import MONGODB


class MongoService():
    LIMIT = 20

    def __init__(self):
        time_pattern = time.strftime('%d_%m_%y')
        connection = pymongo.Connection(MONGODB['HOST'], MONGODB['PORT'])
        db = connection[MONGODB['DB']]
        self.daily = db[MONGODB['MONGODB_COLLECTION_DAILY'] + time_pattern]
        self.active = db[MONGODB['MONGODB_COLLECTION_ACTIVE'] + time_pattern]

    def fetch_all(self):
        return self.daily.find().sort('session', pymongo.ASCENDING)

    def fetch(self):
        return self.fetch(self.LIMIT)

    def fetch(self, limit):
        return self.daily.find().sort('session', pymongo.ASCENDING).limit(limit)

    def fetch_page(self, offset, count):
        return self.daily.find(count=count, offset=offset)