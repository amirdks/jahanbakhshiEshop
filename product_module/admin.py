from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    pass


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    raw_id_fields = ['product']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductGalleryInline
    ]


@admin.register(ProductVisit)
class ProductVisitAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductComment)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_accepted']


@admin.register(ProductVote)
class ProductVoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'vote']


@admin.register(ProductCoupon)
class ProductCouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_code', 'discount_type']
