const formatter = new Intl.NumberFormat('fa-IR', {
    style: 'currency',
    currency: 'IRR',
});
$('#delivery-price').html(formatter.format(15000))

function changeCount(type, id, orderId) {
    let input = document.querySelector(`#cart-quantity-input-${id}`);
    if (type === 'reduce' && input.value === '1') {
        console.log('shit')
    } else {
        let cookie = document.cookie
        let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
        $.ajax({
            method: "POST",
            url: "/order/cart/",
            data: {
                type: type,
                order_detail_id: orderId,
            },
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function (res) {
                if (res.status === 'success') {
                    if (type === 'reduce') {
                        input.stepDown();
                    } else {
                        input.stepUp();
                    }
                    $(`#total-amount-${id}`).html(formatter.format(res.total))
                    $('#total-cart-amount').html(formatter.format(res.total_amount + 15000))
                    $('#total-cart-2-amount').html(formatter.format(res.total_products))
                } else if (res.status === 'error') {
                    console.log('ridi dabsh')
                }
            },
            error: function (res) {
                showNotification({message:'لطفا از اتصال اینترنت خود اطمینان حاصل فرمایید', status:'error'}, 'شکست')
            }
        })
    }
}

function reduceInputValue(id, orderId) {
    changeCount('reduce', id, orderId)
}

function addInputValue(id, orderId) {
    changeCount('add', id, orderId)
}

function deleteProduct(id) {
    let cookie = document.cookie
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
    $.ajax({
        method: "POST",
        url: "/order/cart/",
        data: {
            type: 'delete',
            order_detail_id: id,
        },
        headers: {
            'X-CSRFToken': csrfToken
        },
        success: function (res) {
            if (res.status === 'success') {
                $(`#cart-product-${id}`).fadeOut(1000)
                $(`#total-amount-${id}`).html(formatter.format(res.total))
                $('#total-cart-amount').html(formatter.format(res.total_amount + 15000))
                $('#total-cart-2-amount').html(formatter.format(res.total_products))
                showNotification(res, 'موفق')
            } else if (res.status === 'error') {
                showNotification(res, 'شکست')
            }
        },
        error: function (res) {
            showNotification({message:'لطفا از اتصال اینترنت خود اطمینان حاصل فرمایید', status:'error'}, 'شکست')
        }
    })
}

let couponForm = $('#coupon-form');
couponForm.submit(function (e) {
    e.preventDefault()
    let cookie = document.cookie
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
    $.ajax({
        method: "POST",
        url: e.target.action,
        data: {
            type: 'coupon',
            coupon_code: $('#coupon-code-input').val()
        },
        headers: {
            'X-CSRFToken': csrfToken
        },
        success: function (res) {
            if (res.status === 'success') {
                $('#total-cart-amount').html(formatter.format(res.total_amount + 15000))
                $('#discount-price').html(formatter.format(res.discount_price))
                showNotification(res, 'موفق')
            } else if (res.status === 'error') {
                showNotification(res, 'شکست')
            }
        },
        error: function (res) {
            showNotification({message:'لطفا از اتصال اینترنت خود اطمینان حاصل فرمایید', status:'error'}, 'شکست')
        }
    })
})