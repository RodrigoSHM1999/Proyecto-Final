# Generated by Django 3.1 on 2020-08-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0034_auto_20200817_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='product_id',
            field=models.ManyToManyField(to='market.Product'),
        ),
    ]
