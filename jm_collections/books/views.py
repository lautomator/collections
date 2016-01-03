import re
import random
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from books.models import Publication


def get_queryset():
    ''' Return the last 5 records '''
    return Publication.objects.order_by('-id')[:5]


def get_record_details(pub_id):
    return Publication.objects.get(id=pub_id)


def get_queryset_all():
    ''' Returns every entry '''
    return Publication.objects.all().order_by('id')


def get_categories():
    ''' Returns a list of the long-name categories '''

    categories = Publication.CATEGORIES
    categories_ln = []

    for c in categories:
        categories_ln.append(str(c[1]))

    return categories_ln


def get_category_code(category):
    ''' Returns the 3-letter code from the long name'''

    categories = Publication.CATEGORIES

    for c in categories:
        if str(c[1]) == category:
            return c[0]


def get_long_category(category):
    ''' Returns a single long-name category from the category code '''

    categories = Publication.CATEGORIES

    for c in categories:
        if str(c[0]) == category:
            return c[1]


def check_date(date):
    ''' Return True if any 4 numbers '''

    date_re = re.compile(r'^[0-9]{4}$')
    return date_re.match(date)


def check_entries(title, author, date):
    ''' Checks for valid input and returns messages '''
    params = {}
    if not title:
        params['error_publication_title'] = "Add a title."
    if not author:
        params['error_publication_author'] = "Add an author."
    if not date:
        params['error_publication_date'] = "Add a publication date."
    elif not check_date(date):
        params['error_publication_date'] = "Enter a proper date (i.e., 1945)"

    if params:
        return params


def get_featured():
    # get the publications
    pubs = get_queryset_all()
    # get the length of the publications list
    pub_length = len(pubs) - 1
    # random number
    ran_pub_index = random.randint(0, pub_length)

    return pubs[ran_pub_index].title


def publications_home(request):
    author = request.user
    authenticated = False
    recent_entries = get_queryset()
    featured = get_featured()

    # get the full path of the current page
    # book_path = request.get_full_path()

    if author.is_authenticated():
        authenticated = True

    context = {'recent_entries': recent_entries,
               'author': author,
               'authenticated': authenticated,
               'featured': featured}
    return render(request, 'books/index.html', context)


def publication_details(request, pub_id):
    author = request.user
    authenticated = False
    pub_details = get_record_details(pub_id)
    featured = get_featured()

    if author.is_authenticated():
        authenticated = True

    context = {'author': author,
               'pub_details': pub_details,
               'authenticated': authenticated,
               'featured': featured}
    return render(request, 'books/details.html', context)


def publication_overview(request):
    author = request.user
    authenticated = False
    all_items = get_queryset_all()
    featured = get_featured()

    if author.is_authenticated():
        authenticated = True

    context = {'author': author,
               'all_items': all_items,
               'authenticated': authenticated,
               'featured': featured}
    return render(request, 'books/overview.html', context)


@login_required(login_url='/')
def publication_edit(request, pub_id):
    author = request.user
    authenticated = True
    pub = get_record_details(pub_id)
    current_category = pub.category  # ex., VIS
    categories = get_categories()  # ex., [Visual Arts, ..., ...]
    current_category_ln = get_long_category(current_category)
    featured = get_featured()

    if request.method == 'POST':
        title = request.POST.get("publication_title", '')
        pub_author = request.POST.get("publication_author", '')
        pub_date = request.POST.get("publication_date", '')
        category = request.POST.get("publication_category", '')

        error = check_entries(title, pub_author, pub_date)

        if error:
            context = {'author': author,
                       'pub': pub,
                       'categories': categories,
                       'authenticated': authenticated,
                       'featured': featured}

            context.update(error)
            return render(request, 'books/pub_edit.html', context)

        else:
            # update the record
            pub.title = title
            pub.author = pub_author
            pub.pub_date = pub_date
            pub.category = get_category_code(category)

            pub.save()

            return redirect('/books/overview/')

    context = {'author': author,
               'pub': pub,
               'categories': categories,
               'current_category': current_category,
               'current_category_ln': current_category_ln,
               'authenticated': authenticated,
               'featured': featured}
    return render(request, 'books/pub_edit.html', context)


@login_required(login_url='/')
def publication_add(request):
    author = request.user
    authenticated = True
    categories = get_categories()
    featured = get_featured()

    if request.method == 'POST':
        title = request.POST.get("publication_title", '')
        pub_author = request.POST.get("publication_author", '')
        pub_date = request.POST.get("publication_date", '')
        chosen_category = request.POST.get("publication_category", '')

        error = check_entries(title, pub_author, pub_date)

        if error:
            context = {'author': author,
                       'publication_title': title,
                       'publication_author': pub_author,
                       'publication_date': pub_date,
                       'chosen_category': chosen_category,
                       'categories': categories,
                       'authenticated': authenticated,
                       'featured': featured}

            context.update(error)
            return render(request, 'books/pub_add.html', context)

        else:
            # add the new record
            pub = Publication(title=title,
                              author=pub_author,
                              pub_date=pub_date,
                              category=get_category_code(chosen_category))

            pub.save()

            return redirect('/books/overview/')

    context = {'author': author,
               'categories': categories,
               'authenticated': authenticated,
               'featured': featured}
    return render(request, 'books/pub_add.html', context)


@login_required(login_url='/')
def publication_delete(request, pub_id):
    author = request.user
    authenticated = True
    pub = get_record_details(pub_id)
    featured = get_featured()

    if request.method == 'POST':

        pub.delete()

        return redirect('/books/overview/')

    context = {'author': author,
               'pub': pub,
               'authenticated': authenticated,
               'featured': featured}
    return render(request, 'books/pub_delete.html', context)
