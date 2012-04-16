from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/',include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda x: HttpResponseRedirect('/polls/')),
)
