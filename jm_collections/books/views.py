from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from django.views.generic import DeleteView

from books.models import Publication


def get_queryset():
    ''' Return the last 5 records '''

# TODO: use cache

    return Publication.objects.order_by('-id')[:5]


def get_record_details(pub_id):

    # TODO: use cache

    return Publication.objects.get(id=pub_id)


def get_queryset_all():
    ''' Returns every entry '''

    # TODO: use cache

    return Publication.objects.all().order_by('id')


def get_categories():
    ''' Returns the long-name category '''

    # TODO: use cache

    categories = Publication.CATEGORIES
    category_codes = []

    for c in categories:
        category_codes.append(str(c[1]))

    return category_codes


def get_category_code(category):
    ''' Returns the 3-letter code '''

    # TODO: use cache

    categories = Publication.CATEGORIES

    for c in categories:
        if str(c[1]) == category:
            return c[0]


@login_required(login_url='/')
def publications_home(request):
    author = request.user
    recent_entries = get_queryset()
    context = {'recent_entries': recent_entries,
               'author': author}
    return render(request, 'books/index.html', context)


@login_required(login_url='/')
def publication_details(request, pub_id):
    author = request.user
    pub_details = get_record_details(pub_id)
    context = {'author': author,
               'pub_details': pub_details}
    return render(request, 'books/details.html', context)


@login_required(login_url='/')
def publication_overview(request):
    author = request.user
    all_items = get_queryset_all()
    context = {'author': author,
               'all_items': all_items}
    return render(request, 'books/overview.html', context)


@login_required(login_url='/')
def publication_edit(request, pub_id):
    author = request.user
    pub = get_record_details(pub_id)
    current_category = pub.category
    categories = get_categories()

    if request.method == 'POST':
        pub.title = request.POST.get("publication_title", '')
        pub.author = request.POST.get("publication_author", '')
        pub.pub_date = request.POST.get("publication_date", '')

        category = request.POST.get("publication_category", '')
        pub.category = get_category_code(category)

        pub.save()

        return redirect('/books/overview/')

    # TODO: update cache

    context = {'author': author,
               'pub': pub,
               'categories': categories,
               'current_category': current_category}
    return render(request, 'books/pub_edit.html', context)


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
