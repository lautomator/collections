from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from reader.models import Reader


def get_queryset():
    ''' Return the last 5 reader entries. '''

    reader_entries = Reader.objects.order_by('-id')[:5]
    no_of_entries = len(reader_entries)
    if no_of_entries < 5:
        recent_entries = Reader.objects.order_by('-id')[:no_of_entries]
    else:
        recent_entries = reader_entries
    return recent_entries


def get_queryset_all():
    ''' Return all reader entries. '''
    return Reader.objects.order_by('-id')


def check_entries(title, entry):
    ''' Check for valid input or return a message. '''
    params = {}
    if not title:
        params['error_reader_title'] = "Add a title."
    if not entry:
        params['error_reader_entry'] = "Create an entry."

    if params:
        return params


def reader_home(request):
    author = request.user
    authenticated = False

    if author.is_authenticated():
        authenticated = True

    recent_entries = get_queryset()
    context = {'recent_entries': recent_entries,
               'author': author,
               'authenticated': authenticated}

    return render(request, 'reader/index.html', context)


def reader_overview(request):
    author = request.user
    authenticated = False
    all_items = get_queryset_all()

    if author.is_authenticated():
        authenticated = True

    context = {'all_items': all_items,
               'author': author,
               'authenticated': authenticated}

    return render(request, 'reader/overview.html', context)


@login_required(login_url='/')
def reader_add(request):
    author = request.user

    if request.method == 'POST':
        reader_title = request.POST.get("reader_title", '')
        reader_entry = request.POST.get("reader_entry", '')

        error = check_entries(reader_title, reader_entry)

        if error:
            context = {
                'reader_title': reader_title,
                'author': author,
                'reader_entry': reader_entry
            }
            context.update(error)
            return render(request, 'reader/read_write.html', context)

        else:
            r = Reader.objects
            r.create(reader_title=reader_title,
                     reader_author=author,
                     reader_entry=reader_entry)

            return redirect('/reader/')

    context = {'author': author}

    return render(request, 'reader/read_write.html', context)
