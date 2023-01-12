from django.contrib import admin

# Register your models here.
from order_module.models import Order, OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderDetail)
class OrderDetail(admin.ModelAdmin):
    pass
