import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
django.setup()

from books.models import Book
import random

def generate_random_price():
    for book in Book.objects.all():
        book.price = random.randint(1, 10000) / 100
        book.save()
    return 'Prices generated'

if __name__ == '__main__':
    print(generate_random_price())