from django import forms
from invoices.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['company', 'invoice', 'date', 'amount', 'method', 'payment_number']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'invoice': forms.SelectMultiple(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'date': forms.DateInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'method': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'payment_number': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }
