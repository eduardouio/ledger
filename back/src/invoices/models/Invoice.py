from django.db import models
from common import BaseModel
from companies.models import Company
from accounts.models import CustomUserModel
from inventary.models import Product
from crm.models import Partner


class Invoice(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    type = models.CharField(
        max_length=20,
        choices=(
            ('invoice', 'Invoice'),
            ('bill', 'Bill'))
    )
    date = models.DateField(
        'Date'
    )
    due_date = models.DateField(
        'Due Date'
    )
    number = models.CharField(
        'Document Number',
        max_length=20
    )
    amount = models.DecimalField(
        'Amount',
        max_digits=10,
        decimal_places=2
    )
    discount = models.DecimalField(
        'Discount',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    tax = models.DecimalField(
        'Tax',
        max_digits=10,
        decimal_places=2
    )
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        'Status',
        max_length=20,
        choices=[
            ('draft', 'draft'),
            ('acepted', 'Acepted'),
            ('void', 'Void'),
            ('paid', 'Paid'),
        ],
        default='draft'
    )

    class Meta:
        unique_together = ('company', 'number')

    def __str__(self):
        return self.number

    @classmethod
    def get_by_number(cls, number, name_company):
        company = Company.get_by_name(name_company)
        if not company:
            return []
        return Invoice.objects.get(number=number, company=company)

    @classmethod
    def get_bills(cls, name_company):
        company = Company.get_by_name(name_company)
        if not company:
            raise Exception('Company not found')

        return Invoice.objects.filter(type='bill', company=company)

    @classmethod
    def get_invoices(cls, name_company):
        company = Company.get_by_name(name_company)
        if not company:
            raise Exception('Company not found')

        return Invoice.objects.filter(type='invoice', company=company)


class InvoiceItems(BaseModel):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        'Quantity',
        default=1
    )
    price = models.DecimalField(
        'Price',
        max_digits=10,
        decimal_places=2
    )
    discount = models.DecimalField(
        'Discount',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.product.name
