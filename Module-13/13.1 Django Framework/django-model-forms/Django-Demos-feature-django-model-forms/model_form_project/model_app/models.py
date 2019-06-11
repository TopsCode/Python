from django.db import models

class UserDetails(models.Model):

    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=11,default='123')

    def __str__(self):
        return self.title

