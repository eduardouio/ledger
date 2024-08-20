from django.core.management.base import BaseCommand
from companies.models import Company
from accounts.models import CustomUserModel
import json
import os


class Command(BaseCommand):
    help = 'This command creates a list of users'

    def handle(self, *args, **options):
        print('Creamos empresa base')
        self.LoadBaseEnterprise()
        print('Fin')
        print('Cargamos Cuentas contables')
        self.loadCOAInEnterpise()
        print('Fin')

    def LoadBaseEnterprise(self):
        testCompanie = Company.objects.filter(
            tax_id='9999999999'
        )
        if testCompanie:
            print('Ya Existe, no se crea')
            return True
        myUser = CustomUserModel.get('eduardouio7@gmail.com')
        Company.objects.create(
            tax_id='9999999999',
            name='SYSTEM COMPANY',
            address='Companie sistem for default data',
            manager=myUser
        )

    def loadCOAInEnterpise(self):
        import ipdb;ipdb.set_trace()
        my_company = Company.objects.get_by_tax_id('9999999999')
        if not my_company:
            raise Exception('No existe el cliente System Company')

        file = open('common/accounts.JSON', '+r')
        file.readlines()
