from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
import os
from django.conf import settings



def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class LibrarianView(LibrarianView):
    model = Librarian
    template_name = 'relationship_app/librarian_view.html'
    context_object_name = 'librarian'

class AdminView(AdminView):
    model = Admin
    template_name = 'relationship_app/admin_view.html'
    context_object_name = 'admin'

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


# Role-checking functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin Panel.")

# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian Dashboard.")

# Member View
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to the Member Area.")


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

def custom_render(request, template_name):
    template_path = os.path.join(settings.BASE_DIR, 'relationship_app', template_name)
    with open(template_path, 'r') as f:
        return render(request, template_path)

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    """Check if the user has the 'Admin' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    """View restricted to Admin users."""
    return render(request, 'admin_view.html')


# Create a book (Only for users with 'can_add_book' permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to book list
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

# Edit a book (Only for users with 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

# Delete a book (Only for users with 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

# Role-based access checks
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')  # ✅ No "relationship_app/" prefix

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')  # ✅ No "relationship_app/" prefix

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')  # ✅ No "relationship_app/" prefix
