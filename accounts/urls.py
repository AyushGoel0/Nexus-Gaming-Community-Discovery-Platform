from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            redirect_authenticated_user=True,
            template_name="accounts/login.html",
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("profile/", views.profile, name="profile"),
    path("", views.accounts_home, name="home"),
]
