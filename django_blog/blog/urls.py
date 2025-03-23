from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", profile, name="profile"),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('tags/<slug:tag_slug>/', TaggedPostListView.as_view(), name='tagged-posts'),
]


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # ✅ Ensure this line exists
    path('post/<int:post_id>/comment/', add_comment, name='comment-add'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_id>/comment/new/', CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-add'),
]