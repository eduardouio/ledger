from django.db import models
from common import BaseModel
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
    code_sku = models.CharField(
        'SKU Code',
        max_length=20,
        unique=True
    )
    code_bars = models.CharField(
        'Bars Code',
        max_length=30,
        unique=True
    )
    name = models.CharField(
        'Product Name',
        max_length=100
    )
    price = models.DecimalField(
        'Product Price',
        max_digits=10,
        decimal_places=2
    )
    cost = models.DecimalField(
        'Product Cost',
        max_digits=10,
        decimal_places=2
    )
    type = models.CharField(
        'Product Type',
        max_length=20,
        choices=[
            ('product', 'Product'),
            ('service', 'Service')
        ],
        default='product'
    )

    class Meta:
        unique_together = ('company', 'name')
        unique_together = ('company', 'code_bars')
        unique_together = ('company', 'code_sku')

    @classmethod
    def get_product_by_code_sku(cls, code_sku, company):
        product = cls.objects.filter(
            code_sku=code_sku,
            company=company
        ).first()
        if product:
            return product

        return []

    @classmethod
    def get_product_by_code_bars(cls, code_bars, company):
        product = cls.objects.filter(
            code_bars=code_bars,
            company=company
        ).first()
        if product:
            return product

        return None

    @classmethod
    def get_product_by_name(cls, name, company):
        product = cls.objects.filter(
            name=name,
            company=company
        ).first()
        if product:
            return product

        return []

    @classmethod
    def get_products(cls, type, company):
        my_company = Company.get_by_name(company)
        return cls.objects.filter(
            type='product',
            company=my_company
        )

    @classmethod
    def get_services(cls, type, company):
        my_company = Company.get_by_name(company)
        return cls.objects.filter(
            type='service',
            company=my_company
        )

    def __str__(self):
        return self.name
