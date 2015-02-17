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
    json_docs = []
    for doc in mongo.fetch_all():
        json_doc = json.dumps(doc, default=json_util.default)
        json_docs.append(json_doc)
    return HttpResponse(json_docs, content_type="application/json")