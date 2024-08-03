## generear pagos para varias facturas

from django.db import models
from common import BaseModel
from companies.models import Company
from invoices.models import Invoice


class Payment(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50,
                              choices=[
                                  ('cash', 'Cash'),
                                  ('credit_card', 'Credit Card'),
                                  ('check', 'Check'),
                                  ('bank_transfer', 'Bank Transfer'),
                                  ('other', 'Other')
                              ])

    def __str__(self):
        return self.invoice.number
