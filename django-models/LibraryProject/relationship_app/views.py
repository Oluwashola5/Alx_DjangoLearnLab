from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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


# User Registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # Redirect to books page after registration
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# User Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")  # Redirect to books page after login
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# User Logout
def logout_view(request):
    logout(request)
    return render(request, "logout.html")
