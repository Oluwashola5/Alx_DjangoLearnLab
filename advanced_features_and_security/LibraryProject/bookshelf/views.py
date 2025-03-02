from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookForm
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic for creating a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic for editing a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

def search_books(request):
    query = request.GET.get('search', '').strip()  # Trim spaces and handle empty input
    books = Book.objects.filter(title__icontains=query)  # Secure ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books})

def my_view(request):
    response = HttpResponse("Secure Page")
    response["Content-Security-Policy"] = "default-src 'self'"
    return response
# Create your views here.

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # Redirect to book listing page
    else:
        form = BookForm()

    return render(request, "bookshelf/book_form.html", {"form": form})
from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # Redirect to book listing page
    else:
        form = BookForm()

    return render(request, "bookshelf/book_form.html", {"form": form})

def example_view(request):
    form = ExampleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Process the form data
        cleaned_data = form.cleaned_data
        print(cleaned_data)  # Replace with actual processing logic
    return render(request, "example_form.html", {"form": form})