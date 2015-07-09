from django.contrib import admin
from books.models import Publication


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'pub_date', 'category']

admin.site.register(Publication, BooksAdmin)
