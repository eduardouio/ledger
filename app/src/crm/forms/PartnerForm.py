from django import forms
from crm.models import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['type', 'company', 'name', 'id_num', 'email', 'pay_terms']
        widgets = {
            'type': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'company': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'id_num': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'payd_terms': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }
