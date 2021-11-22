from django.http.response import Http404
from django.shortcuts import render
from django.views import generic
from .models import Book, Author
from django.http import HttpResponse

def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book


def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")


    book_id=get_object_or_404(Book, pk=1)

    return render(
        request,
        'library/book_detail.html',
        context={'book':book_id,}
    )
class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        search_book = Book.objects.filter(title__contains=searched)
        search_author = Author.objects.filter(last_name__contains=searched)

        return render(request, 'library/search.html',{
            'searched':searched,
            'search_book':search_book,
            'search_author':search_author,
    })
    else:
        return render(request, 'library/search.html',{
    })


   