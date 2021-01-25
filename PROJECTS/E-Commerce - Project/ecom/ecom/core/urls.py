from django.urls import path
from .import views
from .views import (
   
    CheckoutView,
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'core'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('product/<slug>/', ItemDetailView.as_view(), name='product'),
	path('checkout/', CheckoutView.as_view(), name='checkout'),
	path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
	path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
	path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
	path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
	path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
	path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
	path('request-refund/', RequestRefundView.as_view(), name='request-refund')

]