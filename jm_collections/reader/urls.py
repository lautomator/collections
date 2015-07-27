from django.conf.urls import patterns, url

from reader import views

urlpatterns = patterns(
    '',
    # /reader/
    url(r'^$', views.reader_home, name='index'),
    # /reader/overview/
    url(r'^overview/$', views.reader_overview, name='overview'),
    # /reader/<reader_id>/details/
    url(r'^(?P<reader_id>\d+)/details/$', views.reader_details,
        name='details'),
    # /reader/add/
    url(r'^add/$', views.reader_add, name='add')
)
