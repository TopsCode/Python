"""ecommerce URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    
    path("women/", views.women, name = 'women'),
    path("men/", views.men, name = 'men'),
    path("accessories/", views.accessories, name = 'accessories'),
    path('filter/', views.filter, name='filter'),
    
    path("product_single/<int:id><str:title>", views.product_single, name = 'product_single'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("support/", views.support, name='support'),
    path("blog/", views.blog, name='blog'),
    path("blog_single/", views.blog_single, name='blog_single'),
    path("wishlist/", views.wishlist, name='wishlist'),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path("order_complete/", views.order_complete, name='order_complete'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forget_password/', views.forget_password, name='forget_password'),
    
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('forget_password_user/', views.forget_password_user, name='forget_password_user'),
    path('forget_password_otp/', views.forget_password_otp, name='forget_password_otp'),
    path('resend_otp/', views.resend_otp, name='resend_otp'),
    
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),

    path('update_profile_user/', views.update_profile_user, name='update_profile_user'),
    path('change_password_user/', views.change_password_user, name='change_password_user'),

    path('logout/', views.logout, name='logout'),

    path('add_to_cart/', views.addToCart, name='add_to_cart'),
    path('add_to_wishlist/<int:product_id>', views.addToWishlist, name='add_to_wishlist'),
    path('wishlist_to_cart/', views.wishlistToCart, name='wishlist_to_cart'),
    path('remove_from_cart/<int:cart_id>', views.removeFromCart, name='remove_from_cart'),
    path('remove_from_Wishlist/<int:wishlist_id>', views.removeFromWishlist, name='remove_from_wishlist'),
    path('cart_quantity_increment/<int:cart_id>', views.cartQuantityIncrement, name='cart_quantity_increment'),
    path('cart_quantity_Decrement/<int:cart_id>', views.cartQuantityDecrement, name='cart_quantity_decrement'),

    path('place_order/', views.placeOrder, name='place_order'),
    path('orders/', views.orders, name='orders'),
    path('order_single/', views.orderSingle, name='order_single'),
]