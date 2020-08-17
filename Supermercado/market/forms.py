from django import forms
from .models import Product
from .models import Compra
from .models import Client
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'img',
            'price',
            'desc',
            'offer',
        ]

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = [
            'client_id',
            'monto',
            'date',
            'product_id',
        ]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'usuario',
            'email',
            'dni',
            'password1',
            'password2',
            'date',
            'status',
        ]