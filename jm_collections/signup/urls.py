from django.conf.urls import patterns, url

from signup import views

urlpatterns = patterns(
    '',
    # /
    url(r'^$', views.user_login, name='index'),
    # /signup/
    url(r'^signup/$', views.user_signup, name='signup'),
    # /logout/
    url(r'^logout/$', views.user_logout, name='logout')
)
