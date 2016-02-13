from django.conf.urls import patterns, url

from signup import views

urlpatterns = patterns(
    '',
    # /
    url(r'^login/$', views.user_login, name='login'),
    # /signup/
    # url(r'^signup/$', views.user_signup, name='signup'),
    # /logout/
    url(r'^logout/$', views.user_logout, name='logout')
)
