# Generated by Django 3.1 on 2020-08-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0022_compra_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='product_id',
            field=models.ManyToManyField(to='market.Product'),
        ),
    ]
