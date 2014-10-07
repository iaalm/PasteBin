from django.views.generic import RedirectView
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PasteBin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^anonymous/', include('AnonymousBin.urls')),
    url(r'^$', RedirectView.as_view(url='/anonymous/'))
)
