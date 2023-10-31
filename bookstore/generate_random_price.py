import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
django.setup()


def generate_random_price():
    from books.models import Book
    import random
    for book in Book.objects.all():
        book.price = random.randint(5, 19) + 0.99
        book.save()
    return 'Prices generated'


if __name__ == '__main__':
    print(generate_random_price())
