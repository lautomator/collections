from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from reader.models import Reader


@login_required(login_url='/')
class IndexView(ListView):
    template_name = 'reader/index.html'
    context_object_name = 'recent_entries'

    def get_queryset(self):
        ''' Return the last 5 reader entries. '''
        reader_entries = Reader.objects.order_by('-id')[:5]
        no_of_entries = len(reader_entries)
        if no_of_entries < 5:
            recent_entries = Reader.objects.order_by('-id')[:no_of_entries]
        else:
            recent_entries = reader_entries
        return recent_entries


# @login_required(login_url='/')
class OverviewView(ListView):
    template_name = 'reader/overview.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        ''' Return every entry. '''
        return Reader.objects.order_by('-id')


# @login_required(login_url='/')
class ReaderAdd(CreateView):
    model = Reader
    template_name = 'reader/read_write.html'
    success_url = '/reader/'
    fields = [
        'reader_title',
        'reader_author',
        'reader_entry',
    ]
