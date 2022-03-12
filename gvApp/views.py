from django.shortcuts import render
from gvApp.models import Course
from gvApp.serializers import CourseSerializer
from rest_framework import generics

# Create your views here.
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
