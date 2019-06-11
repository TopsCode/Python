from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('userdetails/',views.userDetails,name="userdetails"),
    path('display/',views.userDetails,name="display"),
    
]
