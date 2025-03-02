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

# Django Security Enhancements

## 1. CSRF Protection
- Added `{% csrf_token %}` to all form templates.

## 2. SQL Injection Prevention
- Used Django ORM instead of raw SQL queries.

## 3. Content Security Policy (CSP)
- Configured CSP headers in `settings.py` to prevent unauthorized scripts.

## 4. Testing
- Verified CSRF tokens in forms.
- Attempted SQL injection to confirm protection.
- Checked HTTP headers in browser DevTools.
