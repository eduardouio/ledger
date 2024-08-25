from common import BaseModel
from companies.models import Company
from django.db import models


class Account(BaseModel):
    id = models.AutoField(
        primary_key=True
    )
    code = models.CharField(
        'Account Code',
        max_length=20
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
            ('cost', 'Cost Of Goods Sold'),
            ('expense', 'Expense'),
        ]
    )
    level = models.IntegerField(
        'Account Level',
        default=1
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

    @classmethod
    def get_account(cls, code, company):
        account = cls.objects.filter(code=code, company=company)
        if len(account) == 1:
            return account.first()

        raise Exception('Hubo un error al obtener la cuenta ' + account)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code', 'company'], name='unique_code_company'),
            models.UniqueConstraint(
                fields=['name', 'company', 'level'], name='unique_name_company'),
        ]

    def __str__(self):
        return self.name + ' - ' + self.code
