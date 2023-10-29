from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import urllib.parse
from .forms import SearchForm
from .models import Book


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
        if order == 'asc':
            books = Book.objects.filter(
                title__icontains=search).order_by(sortby)
        else:
            books = Book.objects.filter(
                title__icontains=search).order_by(f'-{sortby}')
    else:
        if order == 'asc':
            books = Book.objects.all().order_by(sortby)
        else:
            books = Book.objects.all().order_by(f'-{sortby}')

    form = SearchForm(request.GET)
    return render(request, 'index.html', {'books': books, 'form': form})


def details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'details.html', {'book': book})
