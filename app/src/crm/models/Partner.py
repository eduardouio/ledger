from common import BaseModel
from companies.models import Company
from django.db import models

PAYD_TERMS = (
    (0, 'Cash'),
    (7, '7 Days'),
    (15, '15 Days'),
    (30, '30 Days'),
    (60, '60 Days'),
)


class Partner(BaseModel):
    id = models.AutoField(primary_key=True)
    type = models.CharField(
        'Supplier Type',
        max_length=50,
        choices=[
            ('supplier', 'Supplier'),
            ('customer', 'Customer'),
        ]
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Supplier Name',
        max_length=100
    )
    id_num = models.CharField(
        'ID Number',
        max_length=20
    )
    email = models.EmailField(
        'Email Address',
        max_length=100,
        blank=True,
        null=True
    )
    payd_terms = models.IntegerField(
        'Payment Terms',
        choices=PAYD_TERMS,
        default=0
    )

    @classmethod
    def get_suppliers(cls, company):
        my_company = Company.get_by_name(company)
        return cls.objects.filter(type='supplier', company=my_company)

    @classmethod
    def get_customers(cls, company):
        my_company = Company.get_by_name(company)
        return cls.objects.filter(type='customer', company=my_company)

    class Meta:
        unique_together = ('company', 'id_num', 'type')

    def __str__(self):
        return 'S' + self.name
