from rest_framework import serializers
from .models import Employee

class Employee_Serializer(serializers.ModelSerializer) :
    name=serializers.CharField(max_length=50)
    age=serializers.IntegerField()
    email=serializers.EmailField()
    number=serializers.IntegerField()

    class Meta :
        model=Employee
        fields='__all__'