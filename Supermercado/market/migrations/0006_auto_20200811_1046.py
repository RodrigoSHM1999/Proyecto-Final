# Generated by Django 3.1 on 2020-08-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20200811_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='archivos'),
        ),
    ]
