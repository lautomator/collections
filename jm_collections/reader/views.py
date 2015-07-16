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


@login_required(login_url='/')
def reader_home(request):
    recent_entries = get_queryset()
    context = {'recent_entries': recent_entries}
    return render(request, 'reader/index.html', context)


@login_required(login_url='/')
def reader_overview(request):
    all_items = get_queryset_all()
    context = {'all_items': all_items}
    return render(request, 'reader/overview.html', context)


def check_entries(t, e):
    params = {}
    if not t or not e:
        params['has_warning'] = "Fill in all fields."

    return params


@login_required(login_url='/')
def reader_add(request):
    reader_title = request.POST.get("reader_title", '')
    reader_author = ''
    reader_entry = request.POST.get("reader_entry", '')

    if reader_title or reader_entry:
        error = check_entries(reader_title, reader_entry)

        if error:
            context = {
                'reader_title': reader_title,
                'reader_author': reader_author,
                'reader_entry': reader_entry
            }
            context.update(error)
            return render(request, 'reader/read_write.html', context)

        else:
            # add entries to db
            r = Reader.objects
            r.create(reader_title=reader_title,
                     reader_author=reader_author,
                     reader_entry=reader_entry)

            # update the cache

            # this could go to a review page

            return redirect('/reader/')

    return render(request, 'reader/read_write.html')
