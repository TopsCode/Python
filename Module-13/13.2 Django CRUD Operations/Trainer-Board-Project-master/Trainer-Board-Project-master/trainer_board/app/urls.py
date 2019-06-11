
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.loginpage,name="login"),
    path('home/',views.home,name="home"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('register/',views.registeruser,name="registeruser"),
    path('login_user/',views.login_check,name="login_user"),
    path('post/',views.post_task,name="post_task"),
    path('userdashboard/',views.userdashboard,name="userdashboard"),
    path('edit/',views.edit_task,name="edit"),
    path('delete/',views.delete_task,name="delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)