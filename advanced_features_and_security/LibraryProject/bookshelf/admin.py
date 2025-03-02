from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from relationship_app.models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Display these fields in the admin list view
    search_fields = ("title", "author")  # Add search functionality
    list_filter = ("publication_year",)  # Filter books by publication year

class CustomUserAdmin(UserAdmin):
    pass  # You can customize this class if needed

admin.site.register(CustomUser, CustomUserAdmin) 

# Get content type for Book model
book_content_type = ContentType.objects.get_for_model(Book)

# Define permissions
permissions = Permission.objects.filter(content_type=book_content_type)

# Create Groups
editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')

# Assign permissions
editors_group.permissions.set(permissions.filter(codename__in=['can_edit', 'can_create']))
viewers_group.permissions.set(permissions.filter(codename__in=['can_view']))
admins_group.permissions.set(permissions)  # Give all permissions

