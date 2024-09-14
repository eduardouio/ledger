from django import forms
from accounting.models import Transaction
from companies.models import Company
from accounts.models import CustomUserModel 

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['company', 'description', 'amount', 'date', 'user']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'rows': 2}),
            'amount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'date': forms.DateInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'type': 'date'}),
            'user': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }
