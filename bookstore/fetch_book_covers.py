# fmt: off
import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
django.setup()

import requests
# fmt: on


def try_get_book_image_url(response, index):
    try:
        return response["items"][index]["volumeInfo"]["imageLinks"]["thumbnail"]
    except KeyError:
        return None


def get_book_image_url(book_title):
    url_title = book_title.replace(" ", "+")
    url_title = url_title.replace("'", "")
    cut_index = url_title.find("(")
    if cut_index != -1:
        url_title = url_title[:cut_index]
    url_title = url_title.strip()

    # fmt: off
    url = f"https://www.googleapis.com/books/v1/volumes?q={url_title}"
    # fmt: on

    response = requests.get(url).json()
    image_url = try_get_book_image_url(response, 0)
    i = 1
    while image_url == None and i < 10:
        image_url = try_get_book_image_url(response, i)
        i += 1

    return image_url


def fetch_book_covers():
    from books.models import Book

    for book in Book.objects.all():
        if not book.cover_image:
            book.cover_image = get_book_image_url(book.title)
            if book.cover_image:
                book.save()
            else:
                print(f"Could not find cover image for {book.title}")

    return "Book covers fetched"


if __name__ == '__main__':
    print(fetch_book_covers())
