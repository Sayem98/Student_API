from rest_framework import serializers
from .models import StudentModel


# Vlidators..

# Create your serializers here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['id', 'name', 'roll', 'city']
