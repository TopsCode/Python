from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=30,blank=True)
    email=models.EmailField(unique= True)
    password=models.CharField(max_length=30)


class task(models.Model):
    user_id=models.CharField(max_length=30,blank=True)
    desc=models.CharField(max_length=300,blank=False)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    status=models.CharField(max_length=30,blank=False)

