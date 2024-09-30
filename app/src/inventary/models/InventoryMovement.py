from django.db import models
from common import BaseModel
from inventary.models import Product
from companies.models import Company
from warenhouses.models import Warenhouse
from accounts.models import CustomUserModel
from accounting.models import Transaction


class InventoryMovement(BaseModel):
    id = models.AutoField(
        primary_key=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    date = models.DateField(
        'Date',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    warenhouse = models.ForeignKey(
        Warenhouse,
        on_delete=models.CASCADE
    )
    description = models.CharField(
        'Description',
        max_length=255
    )
    quantity = models.IntegerField(
        'Quantity',
    )
    cost_per_unit = models.DecimalField(
        'Cost Per Unit',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
        )
    total_cost = models.DecimalField(
        'Total Cost',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    trasanction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    movement = models.CharField(
        'Movement Type',
        max_length=20,
        choices=[
            ('in', 'In'),
            ('out', 'Out')
        ]
    )
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    @classmethod
    def get_by_company(cls, company):
        return cls.objects.filter(
            company=company
        )

    def __str__(self):
        return self.product.name
