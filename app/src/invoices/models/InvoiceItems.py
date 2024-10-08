from django.db import models
from common import BaseModel
from inventary.models import Product


class InvoiceItems(BaseModel):
    id = models.AutoField(
        primary_key=True
    )
    invoice = models.ForeignKey(
        'invoices.Invoice',
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
        decimal_places=2,
        default=0
    )

    @classmethod
    def get_by_invoice(cls, invoice):
        return cls.objects.filter(invoice=invoice)

    def __str__(self):
        return self.product.name
