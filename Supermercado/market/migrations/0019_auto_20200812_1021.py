# Generated by Django 3.1 on 2020-08-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0018_auto_20200812_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='compra_id',
            new_name='product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='compra_id',
            field=models.ManyToManyField(to='market.Client'),
        ),
    ]
