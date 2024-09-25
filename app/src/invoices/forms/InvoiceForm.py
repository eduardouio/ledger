from django import forms
from invoices.models import Invoice
from datetime import datetime


class InvoiceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.today().strftime('%Y-%m-%d')

    class Meta:
        model = Invoice
        fields = ['company', 'partner', 'type', 'date', 'due_date',
                  'pay_term', 'number', 'amount', 'discount', 'tax', 'user',
                  'status'
                  ]
        widgets = {
            'company': forms.Select(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-company'
                }
            ),
            'partner': forms.Select(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-partner'
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-type'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'type': 'date',
                    'id': 'frm-date'
                }
            ),
            'due_date': forms.DateInput(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'type': 'date',
                    'id': 'frm-due_date'
                }
            ),
            'pay_term': forms.Select(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-pay_term'
                }
            ),
            'number': forms.TextInput(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm text-end text-xl text-error',
                    'readonly': 'readonly',
                    'id': 'frm-number'
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm text-end',
                    'id': 'frm-amount'
                }
            ),
            'discount': forms.NumberInput(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-discount'
                }
            ),
            'tax': forms.NumberInput(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-tax'
                }
            ),
            'user': forms.Select(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-user'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'border border-gray-400 p-1 rounded-sm',
                    'id': 'frm-status'
                }
            ),
        }
