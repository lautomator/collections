import re

from django.shortcuts import render
from django.shortcuts import redirect
# from django.http import HttpResponseRedirect
# from django.views.decorators.http import require_http_methods
# from signup.forms import SignupForm
# from django.views.generic import CreateView
# from django.contrib.auth.models import User


# validation directives
_user_re = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
_pw_re = re.compile(r'^.{3,20}$')
_email_re = re.compile(r'^[\S]+@[\S]+\.[\S]+$')


# validate user entries
def valid_username(s):
    return _user_re.match(s)


def valid_password(s1):
    return _pw_re.match(s1)


def valid_verify(s1, s2):
    return s1 == s2


def valid_email(s):
    return _email_re.match(s)


# data entry check
def check_signup(u, p, v, e):
    params = {}

    # run the checks for valid data entry
    if not valid_username(u):
        params['err_name'] = "That's not a valid username."

    if not valid_password(p):
        params['err_password'] = "That's not a valid password."
    elif p != v:
        params['err_verify'] = "Passwords do not match."

    if e and not valid_email(e):
        params['err_email'] = "That's not a valid email."

    return params


def signup(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    verify = request.POST.get("verify", '')
    email = request.POST.get("email", '')

    error = check_signup(username, password, verify, email)




    if have_error:
        context = {
            "username": username,
            "password": password,
            "verify": verify,
            "email": email,
            "err_name": err_name,
            'err_password': err_password,
            'err_verify': err_verify,
            'err_email': err_email
        }

        return render(request, 'signup/signup.html', context)
    else:
        return redirect('/books/')


def login(request):
    return render(request, 'signup/index.html')
