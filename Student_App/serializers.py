from rest_framework import serializers
from .models import StudentModel


# Create your serializers here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['id', 'name', 'roll', 'city']
