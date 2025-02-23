# CRUD Operations in Django Shell

## 1. Create a Book Instance
python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

**Expected Output:**

1984 by George Orwell (1949)


---

## 2. Retrieve the Book
python
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

**Expected Output:**

Title: 1984, Author: George Orwell, Year: 1949


---

## 3. Update the Book Title
python
book.title = "Nineteen Eighty-Four"
book.save()

updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")

**Expected Output:**

Updated Title: Nineteen Eighty-Four


---

## 4. Delete the Book
python
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books.count())

**Expected Output:**

0


---

