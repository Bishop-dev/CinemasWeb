from django.shortcuts import render_to_response
from django.template.context import RequestContext
from movies.mongo_service import MongoService


mongo = MongoService()


def home(request):
    context = RequestContext(request,
                             {'message': 'Hello, World on home page!',
                              'movies': mongo.fetch_all()})
    return render_to_response('items/home.html',
                              context_instance=context)