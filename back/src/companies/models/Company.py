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

    @classmethod
    def get_by_user(self, email):
        user = CustomUserModel.get_by_email(email)
        if user:
            return self.objects.filter(
                manager=user
            )
        raise Exception('User not found')

    @classmethod
    def get_by_tax_id(cls, tax_id):
        company = cls.objects.filter(
            tax_id=tax_id,
        )
        if company:
            return company.first()

    @classmethod
    def get_by_name(cls, name):
        company = cls.objects.filter(
            name=name,
        )
        if company:
            return company.first()

    def __str__(self):
        return self.name
