from django.urls import path
from . import views

urlpatterns = [
    path("", views.TranslateView.as_view(), name="home"),
    path("history", views.HistoryView.as_view(), name="history")
]
