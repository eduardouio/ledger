from common import BaseModel
from companies.models import Company
from django.db import models


class Supplier(BaseModel):
    id = models.AutoField(primary_key=True)
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

    class Meta:
        unique_together = ('company', 'id_num')

    def __str__(self):
        return 'S' + self.name
