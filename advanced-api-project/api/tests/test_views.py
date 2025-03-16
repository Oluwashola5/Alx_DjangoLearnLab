from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book, Author

class BookAPITestCase(TestCase):
    """Test suite for Book API endpoints."""

    def setUp(self):
        """Set up test data before each test case."""
        self.client = APIClient()

        # Create a user and authenticate
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)

        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create test book data
        self.book = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=self.author)

        # API endpoint URLs
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    def test_get_books_list(self):
        """Ensure we can retrieve a list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_book(self):
        """Ensure we can retrieve a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    def test_create_book(self):
        """Ensure an authenticated user can create a new book."""
        new_book_data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, new_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Ensure an authenticated user can update an existing book."""
        updated_data = {"title": "Things Fall Apart - Updated", "publication_year": 1959, "author": self.author.id}
        response = self.client.put(self.detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Things Fall Apart - Updated")

    def test_delete_book(self):
        """Ensure an authenticated user can delete a book."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permission_required(self):
        """Ensure unauthenticated users cannot create a book."""
        self.client.logout()
        new_book_data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, new_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Log in the user
        self.client.login(username="testuser", password="password123")

        # Create a sample book for testing
        self.book = Book.objects.create(title="Sample Book", publication_year=2023)

    def test_create_book_authenticated(self):
        """Test that an authenticated user can create a book"""
        data = {"title": "New Book", "publication_year": 2024}
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)