from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Cart, CartItem, Order
# Create your views here.


def cart(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        Cart.objects.create()
        cart_id = Cart.objects.latest('id').id
        request.session['cart_id'] = cart_id

    cart = Cart.objects.get(pk=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)
    total = cart.total()
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


def removeFromCart(request, book_id):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(pk=cart_id)
    cart.remove_from_cart(request, book_id)

    return HttpResponseRedirect(reverse('cart'))


def checkout(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(pk=cart_id)
    order, created = Order.objects.get_or_create(cart=cart)
    return render(request, 'checkout.html', {'order': order})


def completeOrder(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.complete_order(request=request)
    return render(request, 'orderComplete.html')
