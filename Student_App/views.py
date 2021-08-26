from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StudentModel
from .serializers import StudentSerializer


# Create your views here.

# ====== Function based api view ==========
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def StudentsView(request, pk=None):
    if request.method == 'GET':

        # id = request.data.get(id) Why? local variable id referenced before assignment.(P)--> get('id')
        # id = request.data.get('id')
        id = pk

        if id is not None:
            stu = StudentModel.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = StudentModel.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        # id = request.data.get('id')
        stu = StudentModel.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        # id = request.data.get('id')
        stu = StudentModel.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'data deleted'})

    if request.method == 'PATCH':
        # id = request.data.get('id')
        stu = StudentModel.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated'})
        return Response(serializer.errors)

# ======== class based api view =========
