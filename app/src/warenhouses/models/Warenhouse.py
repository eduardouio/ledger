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

    @classmethod
    def get_warenhouses(cls, company):
        my_company = Company.get_by_name(company)
        if not my_company:
            raise Exception('Company not found')

        return Warenhouse.objects.filter(company=my_company)

    def __str__(self):
        return self.name
