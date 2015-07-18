from django.conf.urls import patterns, url

from reader import views

urlpatterns = patterns(
    '',
    # /reader/
    url(r'^$', views.reader_home, name='index'),
    # /reader/overview/
    url(r'^overview/$', views.reader_overview, name='overview'),
    # /reader/add/
    url(r'^add/$', views.reader_add, name='add')
)
