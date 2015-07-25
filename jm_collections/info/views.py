from django.shortcuts import render


def about(request):
    author = request.user
    authenticated = False

    if author.is_authenticated():
        authenticated = True

    context = {'author': author,
               'authenticated': authenticated}

    return render(request, 'info/about.html', context)
