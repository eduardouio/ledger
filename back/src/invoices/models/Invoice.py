from django.db import models
from common import BaseModel
from companies.models import Company
from accounts.models import CustomUserModel
from inventary.models import Product
from crm.models import Customer, Supplier


class Invoice(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        'crm.Customer',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    supplier = models.ForeignKey(
        'crm.Supplier',
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
    date = models.DateField()
    due_date = models.DateField()
    number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('generated', 'Generated'),
            ('cancelled', 'Cancelled')
        ],
        default='generated'
    )

    def __str__(self):
        return self.number


class InvoiceItems(BaseModel):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        'Quantity',
        default=1
    )
    price = models.DecimalField(
        'Price',
        max_digits=10,
        decimal_places=2
    )
    discount = models.DecimalField(
        'Discount',
        max_digits=10,
        decimal_places=2
    )
    amount = models.DecimalField(
        'Amount',
        max_digits=10,
        decimal_places=2
    )
    tax = models.DecimalField(
        'Tax',
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.product.name
