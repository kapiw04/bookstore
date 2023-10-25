# Generated by Django 4.2.6 on 2023-10-25 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AddField(
            model_name='book',
            name='first_published',
            field=models.PositiveIntegerField(default=1900, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='original_language',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='sales_in_millions',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
    ]
