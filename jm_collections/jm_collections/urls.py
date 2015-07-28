from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('info.urls', namespace="info")),
    url(r'^books/', include('books.urls', namespace="books")),
    url(r'^reader/', include('reader.urls', namespace="reader")),
    url(r'^signup/', include('signup.urls', namespace="signup"))
)
