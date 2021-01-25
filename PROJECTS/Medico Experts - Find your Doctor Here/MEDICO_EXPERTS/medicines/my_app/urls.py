"""medicines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from my_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('registerpage/',views.registerpage,name='registerpage'),
    path('register_user/',views.register_user,name='register_user'),
    path('registerpatient',views.registerpatient,name="registerpatient"),

#    path('registeruser/',views.registeruser,name='registeruser'),
#    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('forgotpage',views.forgotpage,name="forgotpage"),
    path('resetpassword',views.resetpassword,name="resetpassword"),
    path('logout',views.logout,name="logout"),
    path('login_evalute',views.login_evalute,name="login_evalute"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('send-otp/',views.send_otp,name="send-otp"),
    path('resetpassword/',views.resetpassword,name="resetpassword"),
    path('medicines_desc/',views.medicines_desc,name="medicines_desc"),
    path('product/',views.product,name="product"),
    path('medicalshops/',views.medicalshops,name="medicalshops"),
    path('medicalshops/',views.medicalshops,name="medicalshops"),
    path('Adhlist/',views.Adhlist,name="Adhlist"),
    path('filter/<slug:name>',views.filter,name="filter"),
    
]
