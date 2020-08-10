from django.db import models

# Create your models here.

class Product(models.Model):
	id = models.IntegerField
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	price = models.IntegerField()
	desc = models.IntegerField()
	offer = models.BooleanField(default=False)