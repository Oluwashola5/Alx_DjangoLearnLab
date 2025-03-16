from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Author(models.Model):
    """
    Represents an author with a name.
    """
    name = models.CharField(max_length=255)

class Book(models.Model):
    """
    Represents a book with a title, publication year, and an associated author.
    Uses a ForeignKey relationship to Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

# Create your models here.
