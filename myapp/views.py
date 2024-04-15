from django.shortcuts import render
from .models import Employee
from rest_framework.views import APIView
from.serializers import Employee_Serializer
from rest_framework.response import Response
from rest_framework import status

class Myapp(APIView):
    def get(self,request):
        users=Employee.objects.all()
        serializer=Employee_Serializer(users,many=True)
        return Response(serializer.data)
    
    def post(self,request) :
        serializer=Employee_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

class GUDapp(APIView) :
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer=Employee_Serializer(employee)
        return Response(serializer.data)

    def put(self,request,pk):
        employee=self.get_object(pk)
        serializer=Employee_Serializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)      


