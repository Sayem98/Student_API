from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets


# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print('***********List********')
        print('Basename:', self.basename)
        print('Action:', self.action)
        print('Detail:', self.detail)
        print('Suffix:', self.suffix)
        print('Name:', self.name)
        print('Description', self.description)
        stu = StudentModel.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('***********Retrieve********')
        print('Basename:', self.basename)
        print('Action:', self.action)
        print('Detail:', self.detail)
        print('Suffix:', self.suffix)
        print('Name:', self.name)
        print('Description', self.description)
        stu = StudentModel.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def create(self, request):
        print('***********Create********')
        print('Basename:', self.basename)
        print('Action:', self.action)
        print('Detail:', self.detail)
        print('Suffix:', self.suffix)
        print('Name:', self.name)
        print('Description', self.description)
        deserializer = StudentSerializer(request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response({'msg': 'Student created'}, status=status.HTTP_201_CREATED)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print('***********Update********')
        print('Basename:', self.basename)
        print('Action:', self.action)
        print('Detail:', self.detail)
        print('Suffix:', self.suffix)
        print('Name:', self.name)
        print('Description', self.description)
        stu = StudentModel.objects.get(id=pk)
        deserializer = StudentSerializer(stu, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response({'msg': 'data updated'})
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        print('***********Partial Update********')
        print('Basename:', self.basename)
        print('Action:', self.action)
        print('Detail:', self.detail)
        print('Suffix:', self.suffix)
        print('Name:', self.name)
        print('Description', self.description)
        stu = StudentModel.objects.get(id=pk)
        deserializer = StudentSerializer(stu, data=request.data, partial=True)
        if deserializer.is_valid():
            deserializer.save()
            return Response({'msg': 'Partial data updated'})
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        print('***********Destroy********')
        print('Basename:', self.basename)
        print('Action:', self.action)
        print('Detail:', self.detail)
        print('Suffix:', self.suffix)
        print('Name:', self.name)
        print('Description', self.description)
        stu = StudentModel.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'Data deleted'})
