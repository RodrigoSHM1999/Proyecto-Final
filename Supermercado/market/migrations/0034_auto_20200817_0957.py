# Generated by Django 3.1 on 2020-08-17 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0033_delete_cartproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('compra_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.compra')),
                ('products_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='product_id',
            field=models.ManyToManyField(through='market.CartProduct', to='market.Product'),
        ),
    ]
