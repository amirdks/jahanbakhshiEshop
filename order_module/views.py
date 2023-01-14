import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpRequest, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.utils.safestring import mark_safe
from django.views import View

from order_module.models import Order, OrderDetail
from product_module.models import Product, ProductCoupon


class CartView(LoginRequiredMixin, View):
    def total_price(self, order_detail, request):
        order = Order.objects.get(is_paid=False, user_id=request.user.id)
        total = order_detail.get_total_price()
        total_products = order.calculate_products_price
        total_amount = order.calculate_total_price()
        return total, total_amount, total_products

    def get(self, request):
        current_order, created = Order.objects.prefetch_related('orderdetail_set',
                                                                'orderdetail_set__product').get_or_create(is_paid=False,
                                                                                                          user_id=request.user.id)
        total_amount = current_order.calculate_products_price
        context = {
            'order': current_order,
            'sum': total_amount,
            'sum_plus': current_order.calculate_total_price() + 15000,
        }
        return render(request, 'order_module/cart.html', context)

    def post(self, request):
        request_type = request.POST.get('type')
        if request_type == 'coupon':
            order = Order.objects.get(is_paid=False, user_id=request.user.id)
            order_coupon = ProductCoupon.objects.filter(coupon_code__exact=request.POST.get('coupon_code'),
                                                        expires_date__gte=datetime.datetime.now())
            if order_coupon.exists():
                order.discount = order_coupon.first()
                order.save()
                total_amount = order.calculate_total_price()
                return JsonResponse(
                    {'status': 'success', 'total_amount': total_amount, 'discount_price': order.get_discount_price,
                     'message': 'کد تخفیف شما با موفقیت اعمال شد'})
            else:
                return JsonResponse(
                    {'status': 'error', 'message': 'کد تخفیف وارد شده یافت نشد'})
        order_detail_id = request.POST.get('order_detail_id')
        order_detail = OrderDetail.objects.get(id=order_detail_id, order__user_id=request.user.id)
        if request_type == 'reduce':
            if order_detail.count == 1:
                return JsonResponse({'status': 'error'})
            order_detail.count -= 1
            order_detail.save()
            total, total_amount, total_products = self.total_price(order_detail, request)
            total = str(total)
            return JsonResponse(
                {'status': 'success', 'total': total, 'total_products': total_products, 'total_amount': total_amount})
        elif request_type == 'add':
            order_detail.count += 1
            order_detail.save()
            total, total_amount, total_products = self.total_price(order_detail, request)
            return JsonResponse(
                {'status': 'success', 'total_products': total_products, 'total': total, 'total_amount': total_amount})
        elif request_type == 'delete':
            order_detail.delete()
            total, total_amount, total_products = self.total_price(order_detail, request)
            return JsonResponse(
                {'status': 'success', 'total': total, 'total_products': total_products, 'total_amount': total_amount,
                 'message': 'محصول مورد نظر شما با موفقیت حذف شد'})
        else:
            return JsonResponse({'status': 'error'})


def add_product_to_order(request: HttpRequest):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        count = int(request.POST.get('count'))
        if count < 1:
            # count = 1
            return JsonResponse({
                'status': 'error',
                'message': 'مقدار وارد شده معتبر نمی باشد',
            })

        if request.user.is_authenticated:
            product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
            if product is not None and product.quantity > 0:
                current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
                current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
                if current_order_detail is not None:
                    current_order_detail.count += count
                    current_order_detail.save()
                else:
                    new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                    new_detail.save()

                return JsonResponse({
                    'status': 'success',
                    'message': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                })
            else:
                return JsonResponse({
                    'status': 'not_found',
                    'message': 'محصول مورد نظر یافت نشد',
                })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید',
            })
    else:
        return HttpResponseForbidden('شما اجازه ی ورود به این صفحه را ندارید 403')
