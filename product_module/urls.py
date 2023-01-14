from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list_view'),
    re_path(r'cat/(?P<cat>[-\w]+)/', views.ProductListView.as_view(), name='product_categories_list'),
    re_path(r'(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='product_detail_view')
]
