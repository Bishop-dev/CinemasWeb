from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World!")


def detail(request, movie_id):
    return HttpResponse("You are looking at question %s" % movie_id)


def results(request, movie_id):
    response = "You are looking at the results of movie %s"
    return HttpResponse(response % movie_id)


def vote(request, movie_id):
    return HttpResponse("You are voting on movie %s" % movie_id)