from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    url(r'^signup/', include('signup.urls', namespace="signup")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls', namespace="books")),
    url(r'^reader/', include('reader.urls', namespace="reader")),
    url(r'^info/', include('info.urls', namespace="info")),
)
