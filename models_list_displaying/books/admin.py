from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'pub_date',)
    # list_filter = ['autor', 'pub_date', ]


admin.site.register(Book, BookAdmin)
