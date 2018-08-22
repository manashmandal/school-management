from django.urls import path
from .views import ListTeacher, DetailTeacher

urlpatterns = [
    path('teacher/', ListTeacher.as_view()),
    path('teacher/<int:pk>', DetailTeacher.as_view()),
]
