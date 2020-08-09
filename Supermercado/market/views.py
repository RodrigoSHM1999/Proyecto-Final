from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):

	product1 = Product()
	product1.name = 'Pimenton'
	product1.price = '2.00'
	product1.desc = '2.50'


	return render(request, "index.html", {'product1': product1})