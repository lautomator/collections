from django.shortcuts import render


def about(request):
    author = request.user
    authenticated = False
    has_no_sidebar = True

    if author.is_authenticated():
        authenticated = True

    context = {'author': author,
               'authenticated': authenticated,
               'has_no_sidebar': has_no_sidebar}

    return render(request, 'info/index.html', context)
