from django.conf.urls import patterns, url

from info import views

urlpatterns = patterns(
    '',
    # /info/about/
    url(r'^about/$', views.about, name='about'),
)
