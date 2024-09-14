from django import forms
from accounting.models import GeneralLedger
from companies.models import Company
from accounting.models import Account, Transaction

class GeneralLedgerForm(forms.ModelForm):
    class Meta:
        model = GeneralLedger
        fields = ['company', 'account', 'transaction', 'debit', 'credit', 'balance', 'description']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'account': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'transaction': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'debit': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'credit': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'balance': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'rows': 2}),
        }

