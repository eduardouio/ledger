from django import forms
from invoices.models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['company', 'partner', 'type', 'date', 'due_date', 'number', 'amount', 'discount', 'tax', 'user', 'status']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'partner': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'type': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'date': forms.DateInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'type': 'date'}),
            'due_date': forms.DateInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'type': 'date'}),
            'number': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'amount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'discount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'tax': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'user': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'status': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }