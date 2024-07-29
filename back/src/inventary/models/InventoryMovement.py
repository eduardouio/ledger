from django.db import models
from common.models import BaseModel
from .Product import Product
from companies.models import Company


class InventoryMovement(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    movement = models.CharField(
        max_length=20,
        choices=[
            ('in', 'In'),
            ('out', 'Out')
        ]
    )

    def __str__(self):
        return self.product.name
