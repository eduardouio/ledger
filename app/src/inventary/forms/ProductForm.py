from django import forms
from inventary.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['company', 'account', 'code_sku', 'code_bars', 'name', 'price', 'cost', 'type']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'account': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'code_sku': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'code_bars': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'name': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'price': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'cost': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'type': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }