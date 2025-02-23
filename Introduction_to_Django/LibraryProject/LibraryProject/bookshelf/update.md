book.title = "Nineteen Eighty-Four"
book.save()

updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")  # Expected Output: Nineteen Eighty-Four
