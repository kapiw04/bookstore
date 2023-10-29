import os
import django
import random
from django.db.models import Q

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
django.setup()


def fill_with_random():
    from books.models import Book, Genre
    books_to_update = Book.objects.filter(
        # null genre is id 58
        Q(genre__isnull=True) | Q(genre=58) | Q(sales_in_millions__isnull=True)
    )

    count_before = books_to_update.count()

    all_genres = list(Genre.objects.all().exclude(id=58))

    print(Genre.objects.count())  # should return a non-zero value

    for book in books_to_update:

        if book.genre is None or book.genre.id == 58:
            book.genre = random.choice(all_genres)

        if book.sales_in_millions is None:
            book.sales_in_millions = random.randint(1, 10)
        book.save(update_fields=['genre', 'sales_in_millions'])
        # print(f'Updated {book.title} with genre '
        #       f'{book.genre.name} and sales {book.sales_in_millions}')

    return f'{count_before} books updated'


if __name__ == '__main__':
    print(fill_with_random())
