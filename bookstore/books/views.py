from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import urllib.parse
from .forms import SearchForm
from .models import Book
from cart.models import Cart


def index(request):
    form = SearchForm(request.POST or None)

    if form.is_valid():
        search = form.cleaned_data['search']
        sortby = form.cleaned_data['sortby']
        order = form.cleaned_data['order']

        query_parameters = urllib.parse.urlencode({
            'search': search,
            'sortby': sortby,
            'order': order,
        })
        url = f"{reverse('index')}?{query_parameters}"
        return HttpResponseRedirect(url)

    search = request.GET.get('search', '')
    sortby = request.GET.get('sortby', 'title')
    order = request.GET.get('order', 'asc')

    if search:
        if sortby == 'title':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.filter(
                title__icontains=search).order_by(f'{order_prefix}title')
        elif sortby == 'author':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.filter(title__icontains=search).order_by(
                f'{order_prefix}author__name')
        elif sortby == 'price':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.filter(
                title__icontains=search).order_by(f'{order_prefix}price')
        elif sortby == 'sales_in_millions':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.filter(title__icontains=search).order_by(
                f'{order_prefix}sales_in_millions')

        form = SearchForm(request.GET)
        return render(request, 'index.html', {'books': books, 'form': form})

    else:
        if sortby == 'title':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.all().order_by(f'{order_prefix}title')
        elif sortby == 'author':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.all().order_by(f'{order_prefix}author__name')
        elif sortby == 'price':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.all().order_by(f'{order_prefix}price')
        elif sortby == 'sales_in_millions':
            order_prefix = '' if order == 'asc' else '-'
            books = Book.objects.all().order_by(
                f'{order_prefix}sales_in_millions')

        form = SearchForm(request.GET)
        return render(request, 'index.html', {'books': books, 'form': form})


def details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'details.html', {'book': book})


def addToCart(request, book_id):
    cart_id = request.session.get('cart_id')
    print(f"cart_id: {cart_id}")
    if not cart_id:
        Cart.objects.create()
        cart_id = Cart.objects.latest('id').id
        request.session['cart_id'] = cart_id

    book = Book.objects.get(pk=book_id)
    cart = Cart.objects.get(pk=cart_id)
    cart.addToCart(request, book)

    return HttpResponseRedirect(reverse('index'))
