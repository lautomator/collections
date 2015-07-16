from django.shortcuts import render
# from django.views.generic import CreateView
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


# @login_required(login_url='/')
def reader_add(request):
    pass


# class ReaderAdd(CreateView):
#     model = Reader
#     template_name = 'reader/read_write.html'
#     success_url = '/reader/'
#     fields = [
#         'reader_title',
#         'reader_author',
#         'reader_entry',
#     ]
