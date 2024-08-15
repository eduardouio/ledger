from common import BaseModel
from companies.models import Company
from accounting.models import Account
from django.db import models


class GeneralLedger(BaseModel):
    id = models.AutoField(
        primary_key=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )
    transaction = models.ForeignKey(
        'accounting.Transaction',
        on_delete=models.CASCADE
        )
    debit = models.DecimalField(
        'Debit Amount',
        max_digits=10,
        decimal_places=2
    )
    credit = models.DecimalField(
        'Credit Amount',
        max_digits=10,
        decimal_places=2
    )
    balance = models.DecimalField(
        'Balance',
        max_digits=10,
        decimal_places=2
    )
    description = models.TextField(
        'Description',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.description
