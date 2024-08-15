from django.db import models
from common import BaseModel
from companies.models import Company


class Warenhouse(BaseModel):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    code = models.CharField(
        'Warenhouse Code',
        max_length=20
    )
    name = models.CharField(
        'Warenhouse Name',
        max_length=100
    )
    address = models.CharField(
        'Warenhouse Address',
        max_length=100
    )

    class Meta:
        unique_together = ('company', 'code')

    def __str__(self):
        return self.name
