from bson.objectid import ObjectId
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from movies.mongo_service import MongoService
import json
from bson import json_util

mongo = MongoService()


def home(request):
    context = RequestContext(request,
                             {'message': 'Hello, World on home page!'})
    return render_to_response('items/home.html',
                              context_instance=context)


def start(request):
    return HttpResponse(fetch_json_from_cursor(mongo.fetch_default_limit()), content_type="application/json")


def additional(request, last_movie_id):
    _id = ObjectId(str(last_movie_id))
    return HttpResponse(fetch_json_from_cursor(mongo.fetch_page(_id)), content_type="application/json")


def fetch_json_from_cursor(cursor):
    json_docs = []
    for doc in cursor:
        json_docs.append(doc)
    return json.dumps(json_docs, default=json_util.default)