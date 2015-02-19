from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cinemas_web.views.home', name='home'),
    url(r'^movies/start', 'cinemas_web.views.start'),
    url(r'^movies/', include('movies.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
