from django.db import models
from common.models import BaseModel
from companies.models import Company
from accounting.models import Account


class Product(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )
    type = models.CharField(
        max_length=20,
        choices=[
            ('product', 'Product'),
            ('service', 'Service')
        ],
        default='product'
    )

    def __str__(self):
        return self.name
