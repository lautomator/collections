import re

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# validation regexes
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


# check for an existing user
def get_user(u, p):
    user = authenticate(username=u, password=p)
    if user is not None:
        if user.is_active:
            return True


# run the checks for data entry and unique, valid user
def check_signup(u, p, v, e):
    params = {}

    if not valid_username(u):
        params['err_name'] = "That's not a valid username."
    elif get_user(u, p):
        params['err_name'] = "That user already exists."

    if not valid_password(p):
        params['err_password'] = "That's not a valid password."
    elif p != v:
        params['err_verify'] = "Passwords do not match."

    if e and not valid_email(e):
        params['err_email'] = "That's not a valid email."

    if params:
        return params


def signup(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    verify = request.POST.get("verify", '')
    email = request.POST.get("email", '')

    if username or password or email or verify:
        error = check_signup(username, password, verify, email)

        if error:
            context = {
                'username': username,
                'password': password,
                'verify': verify,
                'email': email
            }
            context.update(error)
            # has warnings; re-render the page with warnings
            return render(request, 'signup/signup.html', context)
        else:
            User.objects.create_user(username, email, password)
            print 'DB QUERY'  # can log a db query

            return redirect('/')

    return render(request, 'signup/signup.html')


def login(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')

    if username and password:
        if get_user(username, password) is None:
            print get_user(username, password)
            has_warning = 'invalid login'
            context = {'has_warning': has_warning}
            return render(request, 'signup/index.html', context)
        else:
            return redirect('/reader')

    return render(request, 'signup/index.html')


def logout(request):
    pass
