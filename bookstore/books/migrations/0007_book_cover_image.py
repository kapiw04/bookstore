# Generated by Django 4.2.6 on 2023-10-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.URLField(null=True),
        ),
    ]
