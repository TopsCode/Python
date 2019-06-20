from django.db import models

# Create your models here.

class user(models.Model):
    firstname= models.CharField(max_length=250)
    lastname= models.CharField(max_length=250)
    mobile= models.CharField(max_length=11)
    profile_pic=models.FileField(upload_to='images/',default='set.jpg')
    