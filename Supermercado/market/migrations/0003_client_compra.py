# Generated by Django 3.1 on 2020-08-10 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20200809_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='fecha regitro')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='fecha de compra ')),
                ('client_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.client')),
            ],
        ),
    ]