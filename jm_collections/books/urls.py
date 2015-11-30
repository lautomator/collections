from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns(
    '',
    # /books/
    url(r'^$', views.publications_home, name='index'),
    # /books/<pub_id>/details/
    url(r'^(?P<pub_id>\d+)/details/$', views.publication_details,
        name='details'),
    # /books/overview/
    url(r'^overview/$', views.publication_overview, name='overview'),
    # /books/add/
    url(r'^add/$', views.publication_add, name='add'),
    # /books/<pub_id>/edit/
    url(r'^(?P<pub_id>\d+)/edit/$', views.publication_edit, name='edit'),
    # /books/<pub_id>/delete/
    url(r'^(?P<pub_id>\d+)/delete/$', views.publication_delete,
        name='delete')
)
