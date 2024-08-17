from django.core.management.base import BaseCommand
from companies.models import Company
from accounts.models import CustomUserModel


class Command(BaseCommand):
    help = 'This command creates a list of users'

    def handle(self, *args, **options):
        print('Creamos empresa base')
        self.LoadBaseEnterprise()
        print('Fin')
        print('Cargamos Cuentas contables')
        self.loadCOA()
        print('Fin')

    def LoadBaseEnterprise(self):
        testCompanie = Company.objects.filter(
            tax_id='9999999999'
        )
        if testCompanie:
            print('Ya Existe, no se crea')
            return True

        myUser = CustomUserModel.objects.get('eduardouio7@gmail.com')
        Company.objects.create(
            tax_id='9999999999',
            name='SYSTEM COMPANY',
            address='Companie sistem for default data',
            manager=myUser
        )

    def loadCOA(self):
        pass
