from common import BaseModel
from accounts.models import CustomUserModel
from django.db import models


class Company(BaseModel):
    id = models.AutoField(primary_key=True)
    tax_id = models.CharField(
        max_length=20, blank=True, null=True, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    manager = models.ForeignKey(
        'CustomUserModel',
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.name
