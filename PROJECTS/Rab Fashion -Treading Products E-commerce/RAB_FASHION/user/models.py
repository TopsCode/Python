from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 50, blank = True)
    email = models.EmailField(unique = True, blank = False)
    password = models.CharField(max_length = 50, blank = False)
    otp = models.IntegerField(blank = True, default = 0)
    role = models.CharField(max_length = 20, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class ProductManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length = 50, blank = False)
    contact_no = models.CharField(max_length=20, blank = True)
    address = models.CharField(max_length=50, blank = True)
    website = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.company_name

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    address_line_1 = models.CharField(max_length=150, blank = True)
    address_line_2 = models.CharField(max_length=150, blank = True)
    city = models.CharField(max_length=100, blank = True)
    state = models.CharField(max_length=100, blank = True)
    country = models.CharField(max_length=100, blank = True)
    zip_code = models.CharField(max_length=20, blank = True)
    contact_no = models.CharField(max_length=20, blank = True)

class Category (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SubCategory (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ColorVariation (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SizeVariation (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    productManager = models.ForeignKey(ProductManager, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=50)
    image = models.ImageField(upload_to="products/")
    description = models.TextField()
    price = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    available_colors = models.ManyToManyField(ColorVariation)
    available_sizes = models.ManyToManyField(SizeVariation)
    stock = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.productManager.company_name + " : " + self.title

    def colorList(self):
        return [str(color) for color in self.available_colors.all()]

    def sizeList(self):
        return [str(size) for size in self.available_sizes.all()]

class WishlistData(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class CartData(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorVariation, on_delete=models.CASCADE)
    size = models.ForeignKey(SizeVariation, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.customer.user.email + " : " + self.product.productManager.company_name + " : " + self.product.title + " : " + self.color.name + " : " + self.size.name

    def total(self):
        return self.product.price * self.quantity

class Payment(models.Model):
    payment_method = models.CharField(max_length=50, choices=(
        ("Card","Card"),("PayPal","PayPal")
    ))
    amount = models.FloatField()
    successfull = models.BooleanField(default = False)
    payment_date = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(
        ('Ordered','Ordered'),('Shipped','Shipped'),('Dispatched','Dispatched'),('Delivered','Delivered')
    ))
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorVariation, on_delete=models.CASCADE)
    size = models.ForeignKey(SizeVariation, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)

