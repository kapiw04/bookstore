from django.db import models
from django.core.serializers import serialize

# Create your models here.


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField('books.Book', through='CartItem')

    def __str__(self):
        return f'Cart #{self.id}'

    def total(self):
        cart_items = CartItem.objects.filter(cart=self)
        total = 0
        for cart_item in cart_items:
            total += cart_item.get_total()

        return total

    def addToCart(self, request, book):
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

        if CartItem.objects.filter(book=book, cart=cart).exists():
            cart_item = CartItem.objects.get(book=book, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(book=book, cart=cart)

    def remove_from_cart(self, request, book):
        cart_id = request.session.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)

        if CartItem.objects.filter(book=book, cart=cart).exists():
            cart_item = CartItem.objects.get(book=book, cart=cart)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} x {self.quantity}'

    def get_total(self):
        return self.book.price * self.quantity


class Order(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cart = models.OneToOneField('Cart', on_delete=models.SET_NULL, null=True)
    cart_details = models.JSONField(null=True, blank=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'Order #{self.id}'

    def total(self):
        return sum([item.book.price * item.quantity for item in self.cart.cartitem_set.all()])

    def total_items(self):
        return sum([item.quantity for item in self.cart.cartitem_set.all()])

    def total_unique_items(self):
        return len(self.cart.cartitem_set.all())

    def complete_order(self, request):
        cart_id = request.session.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        order = Order.objects.get(cart=cart)

        cart_serialized = serialize('json', [cart])
        cart_items_serialized = serialize('json', cart.cartitem_set.all())

        order.cart_details = {
            'cart': cart_serialized,
            'cart_items': cart_items_serialized
        }

        form = request.POST
        order.name = form['name']
        order.last_name = form['last_name']
        order.email = form['email']
        order.address = form['address']
        order.city = form['city']
        order.state = form['state']
        order.zipcode = form['zipcode']
        order.total = order.total()
        order.complete = True

        order.save()
        del request.session['cart_id']
        cart.delete()
