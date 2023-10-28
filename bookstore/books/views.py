from django.shortcuts import render
from .models import Book
from .forms import SearchForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            sortby = form.cleaned_data['sortby']
            order = form.cleaned_data['order']
            if sortby == 'title':
                if order == 'asc':
                    books = Book.objects.filter(title__icontains=search).order_by('title')
                else:
                    books = Book.objects.filter(title__icontains=search).order_by('-title')
            elif sortby == 'author':
                if order == 'asc':
                    books = Book.objects.filter(title__icontains=search).order_by('author')
                else:
                    books = Book.objects.filter(title__icontains=search).order_by('-author')
            else:
                if order == 'asc':
                    books = Book.objects.filter(title__icontains=search).order_by('price')
                else:
                    books = Book.objects.filter(title__icontains=search).order_by('-price')
            return render(request, 'index.html', {'books': books, 'form': form})
        
    form = SearchForm()    
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})  