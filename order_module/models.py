from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from order_module.validators import min_count_validator


class Order(models.Model):
    user = models.ForeignKey('account_module.User', on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    discount = models.ForeignKey('product_module.ProductCoupon', on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='تخفیف')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return str(self.user)

    @property
    def get_discount_price(self):
        if self.discount:
            total_amount = 0
            if self.is_paid:
                for order_detail in self.orderdetail_set.all():
                    total_amount += order_detail.final_price * order_detail.count
            else:
                for order_detail in self.orderdetail_set.all():
                    total_amount += order_detail.product.price * order_detail.count
            if self.discount.discount_type == 'Price':
                return self.discount.discount_price
            else:
                return self.discount.get_discount_percent * total_amount / 100
        else:
            return 0

    @property
    def calculate_products_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
        return total_amount

    def calculate_total_price(self):
        total_amount = self.calculate_products_price
        if self.discount:
            if self.discount.discount_type == 'Percent':
                total_amount = total_amount - (self.discount.get_discount_percent * total_amount / 100)
            else:
                total_amount = total_amount - self.discount.discount_price
        if total_amount < 0:
            total_amount = 0
        return int(total_amount)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey('product_module.Product', on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(validators=[min_count_validator], verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)


class Shipment(models.Model):
    user = models.ForeignKey('account_module.User', on_delete=models.CASCADE, verbose_name="کاربر")
    first_name = models.CharField(max_length=255, verbose_name="نام گیرنده")
    last_name = models.CharField(max_length=255, verbose_name="نام خانوادگی گیرنده")