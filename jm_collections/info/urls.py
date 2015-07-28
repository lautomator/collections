from django.conf.urls import patterns, url

from info import views

urlpatterns = patterns(
    '',
    # /info/
    url(r'^$', views.about, name='index'),
)
