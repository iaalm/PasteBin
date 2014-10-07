from django.conf.urls import patterns, include, url

from django.contrib import admin
from AnonymousBin.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PasteBin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', create),
    url(r'^(?P<id_num>\d*)/', select)
)
