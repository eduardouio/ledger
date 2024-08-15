from common import BaseModel
from companies.models import Company
from django.db import models


class Account(BaseModel):
    id = models.AutoField(
        primary_key=True
    )
    code = models.CharField(
        'Account Code',
        max_length=20,
        unique=True
    )
    name = models.CharField(
        'Account Name',
        max_length=100
    )
    is_children = models.BooleanField(
        'Account Is Children',
        default=False
    )
    type = models.CharField(
        'Account Type',
        max_length=20,
        choices=[
            ('asset', 'Asset'),
            ('liability', 'Liability'),
            ('equity', 'Equity'),
            ('income', 'Income'),
            ('expense', 'Expense'),
        ]
    )
    description = models.TextField(
        'Account Description',
        blank=True,
        null=True
    )
    parent_account = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name + ' - ' + self.code
