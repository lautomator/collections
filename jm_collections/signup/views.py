from django.shortcuts import render


def index(request):

    # context = {'latest_question_list': latest_question_list}

    print 'signup'
    return render(request, 'signup/index.html')
    # return render(request, 'signup/index.html', context)
