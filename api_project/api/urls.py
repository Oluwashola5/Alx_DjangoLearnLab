from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ListAPIView for read-only books list
    path('books/', BookList.as_view(), name='book-list'),

    # Include all ViewSet routes
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]