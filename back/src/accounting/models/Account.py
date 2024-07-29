from common.models import BaseModel
from companies.models import Company
from django.db import models


class Account(BaseModel):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=20,
        choices=[
            ('asset', 'Activo'),
            ('liability', 'Pasivo'),
            ('equity', 'Patrimonio'),
            ('income', 'Ingreso'),
            ('expense', 'Gasto'),
        ]
    )
    description = models.TextField(blank=True, null=True)
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
        return self.name
