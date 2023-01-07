from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginUser.as_view(), name="login"),
    path("logout", views.LogoutUser.as_view(), name="logout"),
    path("register", views.RegisterUser.as_view(), name="register")
]