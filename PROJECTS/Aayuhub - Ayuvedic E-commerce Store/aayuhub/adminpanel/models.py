from django.db import models

# Create your models here.

class Area(models.Model):
    areaname = models.CharField(max_length = 20)
    
class User(models.Model):
    area_id = models.ForeignKey(Area, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    otp = models.IntegerField(default = 459)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique= True)
    address = models.CharField(max_length= 500, blank = True)
    contact=models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    profile_pic=models.FileField(upload_to='adminpanel/images/',default='Admin.png')

class Product_Manager(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique= True)
    password=models.CharField(max_length = 20)
    brandname=models.CharField(max_length=50)
    brandlogo=models.FileField(upload_to='adminpanel/images/',default='companylogo.png')
    contactno=models.CharField(max_length= 500, blank = True)
    websiteaddress=models.CharField(max_length= 500, blank = True)
    profile_pic=models.FileField(upload_to='adminpanel/images/',default='Admin.png')
    
class Doctor(models.Model):
    name=models.CharField(max_length=60)
    speciality=models.CharField(max_length=60, blank = True)
    contact=models.CharField(max_length=60, blank = True)
    email=models.CharField(max_length=60, blank = True)
    about=models.CharField(max_length=200, blank = True)
    profile_pic=models.FileField(upload_to='images/',default='bg_1.jpg')
    status=models.CharField(max_length=200, blank = True,default="Active")

class yogavideo(models.Model):
    videofile= models.FileField(upload_to='video/', null=True, verbose_name="")

class Category(models.Model):
    catname = models.CharField(max_length = 20)
    catdiscription=models.CharField(max_length=100)
    
class product(models.Model):
    c_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    pname = models.CharField(max_length = 30)
    pdesc = models.CharField(max_length = 500)
    pquantity = models.IntegerField(default=0)
    pprice = models.IntegerField(default=0)
    pexpiredate = models.DateField()
    profile_pic=models.FileField(upload_to='images/',default='bg_1.jpg')

class gallery(models.Model):
    p_id = models.ForeignKey(product, on_delete = models.CASCADE)
    gimage = models.CharField(max_length = 50)

class wishlist(models.Model):
    uid= models.ForeignKey(User, on_delete = models.CASCADE)
    pid= models.ForeignKey(product, on_delete = models.CASCADE)
    qty= models.IntegerField(default=0)
    price= models.IntegerField(default=0)

class addToCart(models.Model):
    uid= models.ForeignKey(User, on_delete = models.CASCADE)
    pid= models.ForeignKey(product, on_delete = models.CASCADE)
    qty= models.IntegerField(default=0)
    price= models.IntegerField(default=0)

class placeOrder(models.Model):
    uid= models.ForeignKey(User, on_delete = models.CASCADE)
    pid= models.ForeignKey(product, on_delete = models.CASCADE)
    qty= models.IntegerField(default=0)
    price= models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    #placed_date=models.DateField(blank=False)
    address=models.CharField(max_length = 150)
    status=models.CharField(max_length=50,default="In Process")

class Feedback(models.Model):
    uid= models.ForeignKey(User, on_delete = models.CASCADE)
    comments=models.CharField(max_length = 150)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    

