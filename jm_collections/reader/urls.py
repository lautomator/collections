from django.conf.urls import patterns, url

from reader import views

urlpatterns = patterns(
    '',
    # /reader/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /reader/overview/
    url(r'^overview/$', views.OverviewView.as_view(), name='overview'),
    # /reader/add/
    url(r'^add/$', views.ReaderAdd.as_view(), name='add')
)
