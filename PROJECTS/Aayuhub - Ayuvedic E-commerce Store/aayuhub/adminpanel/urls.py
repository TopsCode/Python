"""aayuhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('signup-page/',views.signup_page,name="signup-page"),
    path('register_product_manager/',views.register_product_manager,name="register_product_manager"),
    path('admin_login-page/',views.admin_login_page,name="admin_login_page"),
    path('login-evalute/',views.login_evalute,name="login-evalute"),
    path('alogout/',views.alogout,name="alogout"),

    path('doctor-add-page/',views.doctor_add_page,name="doctor-add-page"),
    path('doctor-add/',views.doctor_add,name="doctor-add"),
    path('doctor-view/',views.doctor_view,name="doctor-view"),

    path('video-add-page/',views.video_add_page,name="video-add-page"),
    path('video-add/',views.video_add,name="video-add"),

    path('video-display/',views.video_display,name="video-display"),

    path('category-add-page/',views.category_add_page,name="category-add-page"),
    path('category-add',views.category_add,name="category-add"),
    path('category-list/',views.category_list,name="category-list"),

    path('product-add-list/',views.product_add_page,name="product-add-list"),
    path('product-add/',views.product_add,name="product-add"),
    
    path('product-list/',views.product_list,name="product-list"),
    path('remove-product/<int:pk>',views.remove_product,name="remove-product"),
    path('profile-page/',views.profile_page,name="profile-page"),
    path('admin_update-profile/',views.admin_update_profile,name="admin_update-profile"),
    path('view_feedback/',views.view_feedback,name="view_feedback"),

]