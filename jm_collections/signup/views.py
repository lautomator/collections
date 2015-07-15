import re

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
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

    # run the checks for valid user data entry
    if not valid_username(u):
        params['err_name'] = "That's not a valid username."

    if not valid_password(p):
        params['err_password'] = "That's not a valid password."
    elif p != v:
        params['err_verify'] = "Passwords do not match."

    if e and not valid_email(e):
        params['err_email'] = "That's not a valid email."

    if params:
        return params


# check for an existing user
def get_user(u, p):
    user = authenticate(username=u, password=p)
    if user is not None:
        if user.is_active:
            return True


def signup(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    verify = request.POST.get("verify", '')
    email = request.POST.get("email", '')

    if username or password or email or verify:
        error = check_signup(username, password, verify, email)

        set_user = False

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
            # check that the user does not already exist
            if get_user(username, password):
                set_user = True
            else:
                context = {

                return render(request, 'signup/signup.html', context)



    return redirect('/')

    return render(request, 'signup/signup.html')


def login(request):
    return render(request, 'signup/index.html')
