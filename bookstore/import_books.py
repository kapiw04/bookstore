import os
import django
import csv
from datetime import datetime

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
django.setup()

import csv
from datetime import datetime
from books.models import Book, Author, Genre

def import_books_from_csv(filename):
    with open(filename, 'r', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)
            author, _ = Author.objects.get_or_create(name=row['Author(s)'])
            genre, _ = Genre.objects.get_or_create(name=row['Genre'])
            book = Book(
                title=row['Book'],
                author=author,
                original_language=row['Original language'],
                first_published=int(row['First published']),
                sales_in_millions=int(round(float((row['Approximate sales in millions'])))),
                genre=genre
            )
            book.save()

if __name__ == '__main__':
    import_books_from_csv(r'C:\Users\wojto\OneDrive\Pulpit\PROGRAMOWANIE\PORTFOLIO\BOOKSTORE\best-selling-books.csv')