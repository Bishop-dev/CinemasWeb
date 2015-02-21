from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'cinemas_web.views.home', name='home'),
    url(r'^movies/start', 'cinemas_web.views.start'),
    url(r'^movies/additional/(?P<last_movie_id>\w+)/$', 'cinemas_web.views.additional'),
)
