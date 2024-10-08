from django.db import models
from common import BaseModel
from companies.models import Company
from invoices.models import Invoice


class Payment(BaseModel):
    id = models.AutoField(
        primary_key=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    invoice = models.ManyToManyField(Invoice)
    date = models.DateField(
        'Payment Date'
    )
    amount = models.DecimalField(
        'Amount',
        max_digits=10,
        decimal_places=2
    )
    method = models.CharField(
        'Payment Method',
        max_length=50,
        choices=[
            ('cash', 'Cash'),
            ('credit_card', 'Credit Card'),
            ('check', 'Check'),
            ('bank_transfer', 'Bank Transfer'),
            ('other', 'Other')
        ])
    payment_number = models.CharField(
        'Document Number',
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('company', 'payment_number')

    @classmethod
    def get_payments(cls, company, date_start, date_end):
        my_company = Company.get_by_name(company)
        if not my_company:
            raise Exception('Company not found')

        return Payment.objects.filter(
            company=my_company,
            date__gte=date_start,
            date__lte=date_end
        )

    def __str__(self):
        return self.invoice.number + ' ' + str(self.amount)
