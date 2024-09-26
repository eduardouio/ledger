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