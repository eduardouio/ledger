from django.db import models
from invoices.models import InvoiceItems
from common import BaseModel
from companies.models import Company
from accounts.models import CustomUserModel
from crm.models import Partner

PAYTERM = (
    ('DUE ON RECEIPT', 'DUE ON RECEIPT'),
    ('15 DAYS', '15 DAYS'),
    ('30 DAYS', '30 DAYS'),
    ('60 DAYS', '60 DAYS'),
    ('90 DAYS', '90 DAYS'),
)


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
    pay_term = models.CharField(
        'Payment Term',
        max_length=20,
        choices=PAYTERM
    )
    number = models.IntegerField(
        'Document Number',
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
    def get_by_id(cls, id, company):
        header = Invoice.objects.get(pk=id, company=company)
        if not header:
            raise Exception('Invoice not found')

        items = InvoiceItems.get_by_invoice(header.id)

        return {
            'header': header,
            'items': items
        }

    @classmethod
    def get_by_number(cls, number, company):
        return Invoice.objects.get(number=number, company=company)

    @classmethod
    def get_bills(cls, company):
        return Invoice.objects.filter(
            type='bill', company=company
        )

    @classmethod
    def get_invoices(cls, company):
        return Invoice.objects.filter(
            type='invoice', company=company
        )

    @classmethod
    def get_next_invoice_number(cls, company):
        last = Invoice.objects.filter(company=company).last()
        if not last:
            return 1
        return last.number + 1
