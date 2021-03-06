# Generated by Django 3.1 on 2020-08-12 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20200811_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='compra_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='market.compra'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(max_length=8),
        ),
    ]
