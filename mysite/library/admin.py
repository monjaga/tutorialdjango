from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'books' )
    fields = ['first_name', 'last_name', 'books', ('date_of_birth')]


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_date','display_author', 'image')
    fields = ['title', 'author', 'description',  'added_date', 'image' ]


admin.site.register(Book,BookAdmin)




