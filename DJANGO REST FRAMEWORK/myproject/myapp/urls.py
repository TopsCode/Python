"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_students, name='get_students'),  # GET all students
    path('students/<int:student_id>/', views.get_student, name='get_student'),  # GET a single student by ID
    path('students/create/', views.create_student, name='create_student'),  # POST create a student
    path('students/update/<int:student_id>/', views.update_student, name='update_student'),  # PUT update a student
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),  # DELETE remove a student
]
