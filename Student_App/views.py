from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import StudentModel
from .serializers import StudentSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView,\
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

# ===== Concrete api views =======

class StudentListView(ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveView(RetrieveAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateView(UpdateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentDestroyView(DestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


# ===== combine concrete api view =======


class StudentLCView(ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


# class StudentRUView(RetrieveUpdateAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializer


class StudentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer