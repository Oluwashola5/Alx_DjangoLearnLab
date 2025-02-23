from django.urls import path
from .views import list_books, LibraryDetailView
from .views import BookListView, BookDetailView
from django.urls import path
from .views import register, login_view, logout_view
from .views import admin_view, librarian_view, member_view
from django.urls import path
from .views import admin_view
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('books/', BookListView.as_view(), name='list_books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration view
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
]


urlpatterns = [
    path('admin-dashboard/', admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]

urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
