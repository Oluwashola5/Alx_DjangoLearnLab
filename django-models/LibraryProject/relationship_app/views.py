from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class BookListView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "books"

# DetailView to display details of a single book
class BookDetailView(DetailView):
    model = Book
    template_name = "relationship_app/book_detail.html"
    context_object_name = "book"