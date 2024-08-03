from django.db import models
from common import BaseModel
from .Account import Account
from companies.models import Company


class Bank(BaseModel):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50, choices=[
            ('checking', 'Checking'), ('savings', 'Savings')
    ])
    swift_code = models.CharField(max_length=11, null=True, blank=True)
    routing_number = models.CharField(max_length=9, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('company', 'account_number')

    def __str__(self):
        return self.name + ' - ' + self.company.name
