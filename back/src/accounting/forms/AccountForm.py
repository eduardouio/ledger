from django import forms
from accounting.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['code', 'name', 'is_children', 'type',
                  'level', 'description', 'parent_account', 'company']
        widgets = {
            'company': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-md', 'disabled': 'disabled', 'hidden': 'hidden'}),
            'code': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'name': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'is_children': forms.CheckboxInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'type': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'level': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'parent_account': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'rows': 2}),

        }
