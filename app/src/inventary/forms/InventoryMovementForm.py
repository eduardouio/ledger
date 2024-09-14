from django import forms
from inventary.models import InventoryMovement


class InventoryMovementForm(forms.ModelForm):
    class Meta:
        model = InventoryMovement
        fields = ['company', 'date', 'product', 'warenhouse', 'description', 'quantity', 'cost_per_unit', 'total_cost', 'trasanction', 'movement', 'user']
        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'date': forms.DateInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'type': 'date'}),
            'product': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'warenhouse': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'description': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'quantity': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'cost_per_unit': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'total_cost': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'trasanction': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'movement': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'user': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }