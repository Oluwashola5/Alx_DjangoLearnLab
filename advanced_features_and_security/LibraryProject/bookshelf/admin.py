from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from relationship_app.models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Display these fields in the admin list view
    search_fields = ("title", "author")  # Add search functionality
    list_filter = ("publication_year",)  # Filter books by publication year

class CustomUserAdmin(UserAdmin):
    pass  # You can customize this class if needed

admin.site.register(CustomUser, CustomUserAdmin) 
