from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginUser.as_view(), name="login")
]