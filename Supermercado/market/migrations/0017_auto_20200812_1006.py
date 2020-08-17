# Generated by Django 3.1 on 2020-08-12 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_auto_20200811_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='client_id',
        ),
        migrations.AddField(
            model_name='product',
            name='compra_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='market.compra'),
            preserve_default=False,
        ),
    ]