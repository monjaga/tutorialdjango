from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'books' )
    fields = ['first_name', 'last_name', 'books', ('date_of_birth')]


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','display_author', 'added_date', 'image_tag', 'image')
    fields = ['title', 'author', 'description', 'image']


admin.site.register(Book,BookAdmin)




