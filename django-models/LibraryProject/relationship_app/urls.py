from django.urls import path
from .views import list_books, LibraryDetailView
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('books/', BookListView.as_view(), name='list_books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]