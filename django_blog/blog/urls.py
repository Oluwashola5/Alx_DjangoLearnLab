from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views
from .views import register, profile

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/", profile, name="profile"),
]


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
