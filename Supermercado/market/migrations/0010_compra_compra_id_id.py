# Generated by Django 3.1 on 2020-08-12 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20200811_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='compra_id_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
