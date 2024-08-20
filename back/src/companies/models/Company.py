from common import BaseModel
from accounts.models import CustomUserModel
from django.db import models


class Company(BaseModel):
    id = models.AutoField(primary_key=True)
    tax_id = models.CharField(
        'Tax ID',
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )
    name = models.CharField(
        'Company Name',
        max_length=100
    )
    address = models.CharField(
        'Company Address',
        max_length=255,
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Phone Number',
        max_length=20,
        blank=True,
        null=True
    )
    email = models.EmailField(
        'Email Address',
        max_length=100,
        blank=True,
        null=True
    )
    website = models.URLField(
        'Website',
        max_length=100,
        blank=True,
        null=True
    )
    logo = models.ImageField(
        'Company Logo',
        upload_to='companies/',
        blank=True,
        null=True
    )
    manager = models.ForeignKey(
        CustomUserModel,
        on_delete=models.RESTRICT,
    )

    def get_by_tax_id(self, tax_id):
        company = self.objects.filter(
            tax_id=tax_id,
        )
        if company:
            return company

    def __str__(self):
        return self.name
