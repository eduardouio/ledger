from common import BaseModel
from companies.models import Company
from django.db import models


class Supplier(BaseModel):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    id_num = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('company', 'id_num')

    def __str__(self):
        return 'S' + self.name
