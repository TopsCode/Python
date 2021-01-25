"""vpro URL Configuration

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
    path('index-page/',views.index_page, name='index-page'),
    path('yoga-videos/',views.yoga_video,name="yoga-videos"),
    path('shop-page/',views.shop_page,name="shop-page"),
    path('gallery-page/',views.gallery,name="gallery-page"),
    path('doctor-details/',views.doctor_details,name="doctor-details"),

    path('login-page/',views.login_page, name='login-page'),
    path('login-user/',views.login_user, name='login-user'),

    path('logout/',views.logout_page, name='logout'),
    path(r'^wishlist-add/(?P<pk>\d+)/$', views.wishlist_add, name='wishlist-add'),
    path(r'^wishlist-remove/(?P<pk>\d+)/$', views.wishlist_remove, name='wishlist-remove'),
    


    path('forgot-password/', views.forgot_password, name="forgot-password"),
    path('send-otp/',views.send_otp,name="send-otp"),

    path('registration-page/',views.registration_page, name='registration-page'),
    path('resistration-user/',views.resistration_user, name='resistration-user'),

    path('reset-password/',views.reset_password, name='reset-password'),

    path('profile/', views.profile, name='profile'),

    path('feedback/',views.feedback_page, name='feedback-page'),
    path('about/',views.about_page, name='about-page'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('blog/', views.blog, name='blog'),

    path('cart/', views.cart_page, name='cart-page'),
    path('update-cart/', views.update_cart, name='update-cart'),

    path('checkout/', views.check_out, name='check-out'),
    path('contact/', views.contact_page, name='contact-page'),
    path('product-single/', views.product_single, name='product-single'),

    #path('shop/', views.shop_page, name='shop-page'),
    #path('shop-cart/', views.shop_cart, name='shop-cart'),

    path('wishlist/', views.wish_list, name='wish-list'),
    path('editprofile/', views.edit_profile, name='edit-profile'),
    path('updateprofile/', views.update_profile, name='update-profile'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name="add_to_cart"),
    path('addresspage/<int:pk>',views.addresspage,name="addresspage"),
    path('remove_product/<int:pk>',views.remove_product,name="remove_product"),
    path('placeorder/',views.placeorder,name="placeorder"),
    path('add-feedback/',views.add_feedback,name="add-feedback"),
    
]
