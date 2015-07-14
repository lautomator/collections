import re

from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.views.decorators.http import require_http_methods
# from signup.forms import SignupForm
# from django.views.generic import CreateView
# from django.contrib.auth.models import User


# validation directives
_user_re = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
_pw_re = re.compile(r'^.{3,20}$')
_email_re = re.compile(r'^[\S]+@[\S]+\.[\S]+$')


# valid username and password checks
def valid_username(s):
    return _user_re.match(s)


def valid_password(s1):
    return _pw_re.match(s1)


def valid_verify(s1, s2):
    return s1 == s2


def valid_email(s):
    return _email_re.match(s)


def login(request):
    return render(request, 'signup/index.html')


# class Signup(CreateView):
#     model = User
#     template_name = 'signup/signup.html'
#     success_url = '/reader/'
#     fields = [
#         'username',
#         'password',
#         'verify password',
#         'email',
#     ]


def signup(request):
    return render(request, 'signup/signup.html')
