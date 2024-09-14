from django import forms
from accounting.models import Bank


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['company', 'name', 'account', 'account_number', 'account_type', 'swift_code', 'routing_number', 'address']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'name': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'account': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'account_number': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'account_type': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'swift_code': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'routing_number': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'address': forms.Textarea(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'rows': 2}),
        }

