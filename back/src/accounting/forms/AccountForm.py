from django import forms
from accounting.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['code', 'name', 'is_children', 'type',
                  'level', 'description', 'parent_account', 'company']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
