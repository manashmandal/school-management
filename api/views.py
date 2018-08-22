from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer


# Create your views here.
class ListTeacher(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class DetailTeacher(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer