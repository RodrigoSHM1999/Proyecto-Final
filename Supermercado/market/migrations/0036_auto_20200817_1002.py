# Generated by Django 3.1 on 2020-08-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0035_auto_20200817_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='product_id',
            field=models.ManyToManyField(through='market.CartProduct', to='market.Product'),
        ),
    ]
