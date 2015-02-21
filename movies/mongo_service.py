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
        return self.daily.find({'session': {'$gt': datetime.datetime.now()}}).sort('session', pymongo.ASCENDING).limit(limit)

    def fetch_page(self, offset, count):
        return self.daily.find(count=count, offset=offset)

    def fetch_compressed_default_limit(self):
        return self.db.system_js.compress(self.LIMIT)

    def ensure_compressed_stored_js(self):
        self.db.system_js.compress = "function compress(e){function n(e,n){return e.session==n.session&&e.name==n.name&&e._id!=n._id&&e.cinema!=n.cinema}function i(e,n){var i=e.cinema'string'==typeof i?e.cinema=[i]:e.cinema.push(n.cinema)}for(var t=db.daily_20_02_15.find({session:{$gt:new Date}}).limit(2*e),s=[];t.hasNext();){var a=t.next();if(0!=s.lenght){var r=s[s.length-1];n(r,a)?i(r,a):s.push(a)}else s.push(a);if(t.hasNext()){var f=t.next();if(n(f,a))i(s[s.length-1],f);else{if(s.length==e)return!0;s.push(f)}}for(;t.hasNext()&&s.length==e;){var h=t.next(),c=s[29];if(!n(c,h))break;i(c,h)}}return s}"