
from django import views
from django.urls import path
from .views import Myapp,GUDapp

urlpatterns = [
    path('get',Myapp.as_view()),
    path('GUD/<int:pk>',GUDapp.as_view())

   
]
