from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list_view'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail_view')
]
