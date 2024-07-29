from common import BaseModel
from accounts.models import CustomUserModel
from companies.models import Company
from accounting.models import Account
from django.db import models


class Transaction(BaseModel):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.date} - {self.amount}'
