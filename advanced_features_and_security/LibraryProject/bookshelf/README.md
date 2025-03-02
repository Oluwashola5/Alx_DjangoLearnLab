# Django Permissions and Groups

## Custom Permissions
- `can_view`: Allows users to view books.
- `can_create`: Allows users to create books.
- `can_edit`: Allows users to edit books.
- `can_delete`: Allows users to delete books.

## Groups
- **Viewers**: Can only view books.
- **Editors**: Can create and edit books.
- **Admins**: Have all permissions.

## Setup Instructions
1. Run migrations: `python manage.py makemigrations && python manage.py migrate`
2. Create groups in Django Admin and assign permissions.
3. Assign users to groups in Django Admin.
4. Test by logging in with different users.
