from django.db import models

# Create your models here.
class Client(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=100)
	dni = models.CharField(max_length = 10)
	date = models.DateField('fecha regitro', blank= False,null= False)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Product(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=100, blank=True )
	img = models.ImageField(upload_to='archivos', null=True)
	price = models.IntegerField(null=True)
	desc = models.IntegerField(null=True)
	offer = models.BooleanField(default=False, null=True)
	

# on_delete: al eliminar elimina la relacion 
class Compra(models.Model):
	id = models.AutoField(primary_key = True)
	client_id = models.ForeignKey(Client, on_delete = models.CASCADE)
	monto = models.IntegerField()
	date = models.DateField('fecha de compra ')
	product_id = models.ManyToManyField(Product)
	

	
	


	
	


	







		