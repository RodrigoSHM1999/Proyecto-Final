from django.shortcuts import render
from django.core.mail import send_mail 
from .models import Product
# Create your views here.
def index(request):
	
	send_mail('Hola desde DJANGO',
	'Hello there. This is an automated message.',
	'agarciapu@unsa.edu.pe',
	['agarciapu@unsa.edu.pe'],
	fail_silently=False)

	products = Product.objects.all()

	#product1 = Product()
	#product1.name = 'Pimenton'
	#product1.img = 'product-1.jpg'
	#product1.price = '2.00'
	#product1.desc = '2.50'
	#product1.offer = True

	#product2 = Product()
	#product2.name = 'Fresa'
	#product2.img = 'product-2.jpg'
	#product2.price = '5.00'
	#product2.desc = '2.50'
	#product2.offer = False

	#product3 = Product()
	#product3.name = 'Alverja'
	#product3.img = 'product-3.jpg'
	#product3.price = '2.50'
	#product3.desc = '2.50'
	#product3.offer = False

	#product4 = Product()
	#product4.name = 'Repollo'
	#product4.img = 'product-4.jpg'
	#product4.price = '1.00'
	#product4.desc = '2.50'
	#product4.offer = True

	#products = [product1, product2, product3, product4]	

	return render(request, "index.html", {'products':products})