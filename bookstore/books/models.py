from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    original_language = models.CharField(max_length=50, null=True)
    first_published = models.PositiveIntegerField(null=True, default=1900)
    sales_in_millions = models.PositiveIntegerField(null=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, default=5.99)

    def __str__(self):
        return self.title

    def get_sales_in_millions(self):
        return self.sales_in_millions * 1000000


def generate_random_genre():
    return Genre.objects.get_or_create(name='Random')[0]
