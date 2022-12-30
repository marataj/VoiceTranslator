from django.urls import path
from . import views

urlpatterns = [
    path("", views.TranslateView.as_view()),
    path("voice", views.VoiceRecordView.as_view())
]
