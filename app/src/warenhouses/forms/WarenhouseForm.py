from django import forms
from warenhouses.models import Warenhouse


class WarenhouseForm(forms.ModelForm):
    class Meta:
        model = Warenhouse
        fields = ['company', 'code', 'name', 'address']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'code': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'name': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'address': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }

