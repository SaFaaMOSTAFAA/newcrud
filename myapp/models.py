# from pyexpat import model
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    number=models.IntegerField()

    def __str__(self) :
       return self.name

