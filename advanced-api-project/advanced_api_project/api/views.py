from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define filter fields (for exact match filtering)
    filterset_fields = ['author', 'publication_year']

    # Enable search by title and author name
    search_fields = ['title', 'author__name']

    # Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']

    # Set default ordering (optional)
    ordering = ['title']
