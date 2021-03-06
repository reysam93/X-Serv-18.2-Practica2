from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)$', 'url_shortener.views.redirect'),
    url(r'^$', 'url_shortener.views.processHome'),
)
