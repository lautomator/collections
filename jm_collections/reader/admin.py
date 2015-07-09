from django.contrib import admin
from reader.models import Reader


class ReaderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'reader_title',
        'reader_author',
        'reader_date',
        'reader_entry',
    ]

admin.site.register(Reader, ReaderAdmin)
