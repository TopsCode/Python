from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(ProductManager)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ColorVariation)
admin.site.register(SizeVariation)
admin.site.register(Product)
admin.site.register(WishlistData)
admin.site.register(CartData)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)