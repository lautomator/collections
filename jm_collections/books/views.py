from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

        # TODO: there should be some validation for the data entered

        pub.title = request.POST.get("publication_title", '')
        pub.author = request.POST.get("publication_author", '')
        pub.pub_date = request.POST.get("publication_date", '')

        category = request.POST.get("publication_category", '')
        pub.category = get_category_code(category)

        pub.save()

        # TODO: update cache

        return redirect('/books/overview/')

    context = {'author': author,
               'pub': pub,
               'categories': categories,
               'current_category': current_category}
    return render(request, 'books/pub_edit.html', context)


@login_required(login_url='/')
def publication_add(request):
    author = request.user
    categories = get_categories()

    if request.method == 'POST':
        title = request.POST.get("publication_title", '')
        author = request.POST.get("publication_author", '')
        pub_date = request.POST.get("publication_date", '')
        category = get_category_code(
            request.POST.get("publication_category", ''))

        # TODO: there should be some validation for the data entered

        # add the new record
        pub = Publication(title=title,
                          author=author,
                          pub_date=pub_date,
                          category=category)

        pub.save()

        # TODO update the cache

        return redirect('/books/overview/')

    context = {'author': author,
               'categories': categories}
    return render(request, 'books/pub_add.html', context)


@login_required(login_url='/')
def publication_delete(request, pub_id):
    author = request.user
    pub = get_record_details(pub_id)

    if request.method == 'POST':

        pub.delete()

        # TODO: update the cache

        return redirect('/books/overview/')

    context = {'author': author,
               'pub': pub}
    return render(request, 'books/pub_delete.html', context)
