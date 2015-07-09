from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns(
    '',
    # /books/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /books/<pk>/details/
    url(r'^(?P<pk>\d+)/details/$', views.DetailsView.as_view(),
        name='details'),
    # /books/overview/
    url(r'^overview/$', views.OverviewView.as_view(), name='overview'),
    # /books/<pk>/edit/
    url(r'^(?P<pk>\d+)/edit/$', views.EditView.as_view(), name='edit'),
    # /books/add/
    url(r'^add/$', views.PublicationAdd.as_view(), name='add'),
    # /books/<pk>/delete/
    url(r'^(?P<pk>\d+)/delete/$', views.PublicationDelete.as_view(),
        name='delete'),
)
