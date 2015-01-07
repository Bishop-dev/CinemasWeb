from django.conf.urls import patterns, url
from movies import views

urlpatterns = patterns('',
    # /movies/
    url(r'^$', views.index, name='index'),
    # /movies/5/
    url(r'^(?P<movie_id>\d+)/$', views.detail, name='detail'),
    # /movies/5/results/
    url(r'^(?P<movie_id>\d+)/results/$', views.results, name='results'),
    # /movies/5/vote
    url(r'^(?P<movie_id>\d+)/vote/$', views.vote, name='vote'),
)