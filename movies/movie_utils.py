from movies.mongo_service import MongoService


def start():
    service = MongoService()
    sort_by_date(service.fetch_all())


def sort_by_date(input):
    result = []


start()