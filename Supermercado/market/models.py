from django.db import models

# Create your models here.

class Product(models.Model):
	id = models.IntegerField
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	price = models.IntegerField()
	desc = models.IntegerField()
	offer = models.BooleanField(default=False)
	
class Client(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=100)
	dni = models.IntegerField
	date = models.DateField('fecha regitro', blank= False,null= False)
	status = models.BooleanField(default=False)

#on_delete: al eliminar elimina la relacion 
class Compra(models.Model):
	id = models.AutoField(primary_key = True)
	client_id = models.OneToOneField(Client, on_delete = models.CASCADE)
	monto = models.IntegerField
	date = models.DateField('fecha de compra ', blank = False, null = False)	