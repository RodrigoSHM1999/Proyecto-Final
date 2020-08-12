from django import forms
from .models import Product
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

