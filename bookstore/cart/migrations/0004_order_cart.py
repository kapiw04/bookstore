# Generated by Django 4.2.6 on 2023-10-31 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_order_cart_order_cart_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.cart'),
        ),
    ]
