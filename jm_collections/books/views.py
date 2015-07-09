from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView

from books.models import Publication


class IndexView(ListView):
    template_name = 'books/index.html'
    context_object_name = 'recent_entries'

    def get_queryset(self):
        ''' Return the last 3 entries. '''
        return Publication.objects.order_by('-id')[:3]


class DetailsView(DetailView):
    model = Publication
    template_name = 'books/details.html'


class OverviewView(ListView):
    template_name = 'books/overview.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        ''' Return every entry. '''
        return Publication.objects.all()


class EditView(UpdateView):
    model = Publication
    template_name = 'books/pub_edit.html'
    success_url = '../details/'
    fields = [
        'title',
        'author',
        'pub_date',
        'category',
    ]


class PublicationAdd(CreateView):
    model = Publication
    template_name = 'books/pub_add.html'
    success_url = '../overview/'
    fields = [
        'title',
        'author',
        'pub_date',
        'category',
    ]


class PublicationDelete(DeleteView):
    model = Publication
    template_name = 'books/delete.html'
    success_url = '/books/overview'
