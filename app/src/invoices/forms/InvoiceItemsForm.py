from django import forms
from invoices.models import InvoiceItems

class InvoiceItemsForm(forms.ModelForm):
    class Meta:
        model = InvoiceItems
        fields = ['product', 'quantity', 'price', 'discount']
        widgets = {
            'product': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'quantity': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'price': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'discount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }
