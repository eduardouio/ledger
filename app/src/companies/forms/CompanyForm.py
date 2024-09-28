from django import forms
from companies.models import Company
from accounts.models import CustomUserModel

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'tax_id', 'name', 'address', 'phone', 'email', 'website',
            'logo', 'manager', 'tax_in_sales', 'tax_in_purchases'
        ]
        widgets = {
            'tax_id': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'name': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'address': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'phone': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'website': forms.URLInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'logo': forms.FileInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'manager': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'tax_in_sales': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'tax_in_purchases': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }