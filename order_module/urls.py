from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart_view'),
    path('add-to-order/', views.add_product_to_order, name='add_product_to_order_view'),
]
