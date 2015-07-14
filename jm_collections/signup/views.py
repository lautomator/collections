from django.shortcuts import render


def login(request):
    return render(request, 'signup/index.html')


def signup(request):
    return render(request, 'signup/signup.html')
