from django.shortcuts import render, redirect
from django.core.mail import send_mail 
from .models import *
from .forms import ProductForm
from .forms import CompraForm
from .forms import ClientForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy

class CreateProducto(CreateView):
	model = Product
	form_class = ProductForm
	template_name = 'crear_product.html'
	success_url = reverse_lazy('index')

class ListProducto(ListView):
	model = Product
	template_name = 'listar_product.html'

class UpdateProducto(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'crear_product.html'
	success_url = reverse_lazy('index')

class DeleteProducto(DeleteView):
	model = Product
	template_name = 'eliminar_product.html'
	success_url = reverse_lazy('index')

#Aqui comienza Compra

class CreateCompra(CreateView):
	model = Compra
	form_class = CompraForm
	template_name = 'crear_compra.html'
	success_url = reverse_lazy('index')

class ListCompra(ListView):
	model = Compra
	template_name = 'listar_compra.html'

class UpdateCompra(UpdateView):
	model = Compra
	form_class = CompraForm
	template_name = 'crear_compra.html'
	success_url = reverse_lazy('index')

class DeleteCompra(DeleteView):
	model = Compra
	template_name = 'eliminar_compra.html'
	success_url = reverse_lazy('index')

#Aqui empieza Client

class CreateCliente(CreateView):
	model = Client
	form_class = ClientForm
	template_name = 'crear_client.html'
	success_url = reverse_lazy('index')

class ListCliente(ListView):
	model = Client
	template_name = 'listar_client.html'

class UpdateCliente(UpdateView):
	model = Client
	form_class = ClientForm
	template_name = 'crear_client.html'
	success_url = reverse_lazy('index')

class DeleteCliente(DeleteView):
	model = Client
	template_name = 'eliminar_client.html'
	success_url = reverse_lazy('index')


# Create your views here.
def index(request):
	
	

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

def compra(request):
    return render(request, 'crear_compra.html')

def cliente(request):
    return render(request, 'crear_client.html')

def producto(request):
    return render(request, 'crear_product.html')







		
	