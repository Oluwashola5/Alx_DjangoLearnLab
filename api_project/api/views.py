from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD operations for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
