from django.conf.urls import patterns, url

from info import views

urlpatterns = patterns(
    '',
    # /info/about/
    url(r'^signup/$', views.index, name='signup'),
)
