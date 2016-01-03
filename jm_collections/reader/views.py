import random
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from reader.models import Reader


def get_record_details(reader_id):
    return Reader.objects.get(id=reader_id)


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


def get_featured():
    # get the reader entries
    entries = get_queryset_all()
    # get the length of the entries list
    entry_length = len(entries) - 1
    # random number
    ran_entry_index = random.randint(0, entry_length)

    return entries[ran_entry_index].reader_title


def reader_home(request):
    author = request.user
    authenticated = False
    featured = get_featured()

    if author.is_authenticated():
        authenticated = True

    recent_entries = get_queryset()
    context = {'recent_entries': recent_entries,
               'author': author,
               'authenticated': authenticated,
               'featured': featured
               }

    return render(request, 'reader/index.html', context)


def reader_overview(request):
    author = request.user
    authenticated = False
    all_items = get_queryset_all
    featured = get_featured()

    if author.is_authenticated():
        authenticated = True

    context = {'all_items': all_items,
               'author': author,
               'authenticated': authenticated,
               'featured': featured
               }

    return render(request, 'reader/overview.html', context)


def reader_details(request, reader_id):
    author = request.user
    authenticated = False
    read_details = get_record_details(reader_id)
    featured = get_featured()

    if author.is_authenticated():
        authenticated = True

    context = {'author': author,
               'read_details': read_details,
               'authenticated': authenticated,
               'featured': featured
               }

    return render(request, 'reader/details.html', context)


@login_required(login_url='/')
def reader_add(request):
    author = request.user
    authenticated = True
    featured = get_featured()

    if request.method == 'POST':
        reader_title = request.POST.get("reader_title", '')
        reader_entry = request.POST.get("reader_entry", '')

        error = check_entries(reader_title, reader_entry)

        if error:
            context = {
                'reader_title': reader_title,
                'author': author,
                'reader_entry': reader_entry,
                'authenticated': authenticated,
                'featured': featured}
            context.update(error)
            return render(request, 'reader/read_write.html', context)

        else:
            r = Reader.objects
            r.create(reader_title=reader_title,
                     reader_author=author,
                     reader_entry=reader_entry)

            return redirect('/reader/')

    context = {'author': author,
               'authenticated': authenticated,
               'featured': featured}

    return render(request, 'reader/read_write.html', context)


@login_required(login_url='/')
def reader_edit(request, reader_id):
    author = request.user
    authenticated = True
    read_details = get_record_details(reader_id)
    featured = get_featured()

    if request.method == 'POST':
        read_title = request.POST.get("reader_title", '')
        read_entry = request.POST.get("reader_entry", '')

        error = check_entries(read_title, read_entry)

        if error:
            context = {
                'reader_title': read_title,
                'author': author,
                'reader_entry': read_entry,
                'authenticated': authenticated,
                'featured': featured}

            context.update(error)
            return render(request, 'reader/read_edit.html', context)

        else:
            # update the record
            read_details.reader_title = read_title
            read_details.reader_entry = read_entry

            read_details.save()

            return redirect('/reader/')

    context = {
        'read_details': read_details,
        'reader_id': reader_id,
        'authenticated': authenticated,
        'author': author,
        'featured': featured
    }

    return render(request, 'reader/read_edit.html', context)


@login_required(login_url='/')
def reader_delete(request, reader_id):
    author = request.user
    authenticated = True
    read_details = get_record_details(reader_id)
    featured = get_featured()

    if request.method == 'POST':

        read_details.delete()

        return redirect('/reader/overview/')

    context = {'author': author,
               'read_details': read_details,
               'authenticated': authenticated,
               'featured': featured}

    return render(request, 'reader/read_delete.html', context)
