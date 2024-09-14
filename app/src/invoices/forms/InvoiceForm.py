from django import forms
from app.src.accounts.models import CustomUserModel
from app.src.companies.models import Company
from app.src.crm.models import Partner
from app.src.inventary.models import Product
from invoices.models import Invoice, InvoiceItems

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'company',
            'partner',
            'type',
            'date',
            'due_date',
            'number',
            'amount',
            'discount',
            'tax',
            'user',
            'status',
        ]

        widgets = {
            'company': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'partner': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'type': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'date': forms.DateInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'type': 'date'}),
            'due_date': forms.DateInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm', 'type': 'date'}),
            'number': forms.TextInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'amount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'discount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'tax': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'user': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'status': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.all()
        self.fields['partner'].queryset = Partner.objects.all()
        self.fields['user'].queryset = CustomUserModel.objects.all()

class InvoiceItemsForm(forms.ModelForm):
    class Meta:
        model = InvoiceItems
        fields = [
            'product',
            'quantity',
            'price',
            'discount',
        ]

        widgets = {
            'product': forms.Select(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'quantity': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'price': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
            'discount': forms.NumberInput(attrs={'class': 'border border-gray-400 p-1 rounded-sm'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()