from django.conf.urls import patterns, url

from signup import views

urlpatterns = patterns(
    '',
    # /
    url(r'^$', views.login, name='index'),
    # /signup/
    url(r'^signup/$', views.signup, name='signup'),
)
