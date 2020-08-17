from django.db import models

# Create your models here.
class Client(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=100)
	usuario = models.CharField(max_length=100)
	email = models.EmailField() 
	dni = models.CharField(max_length = 10)
	password1 = models.CharField(max_length = 20, blank= False, null = False)
	password2 = models.CharField(max_length = 20, blank= False, null = False)
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
	def __str__(self):
		return self.name
	

# on_delete: al eliminar elimina la relacion 
class Compra(models.Model):
	id = models.AutoField(primary_key = True)
	client_id = models.ForeignKey(Client, on_delete = models.CASCADE)
	monto = models.IntegerField()
	date = models.DateField('fecha de compra ')
	product_id = models.ManyToManyField(Product, through='CartProduct')

class CartProduct(models.Model):
	compra_id = models.ForeignKey(Compra, on_delete=models.CASCADE)
	products_id = models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)


	

	
	


	
	


	







		