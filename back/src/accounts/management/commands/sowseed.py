from django.core.management.base import BaseCommand
from companies.models import Company
from accounts.models import CustomUserModel
from accounting.models import Account, Bank
from crm.models import Partner
from inventary.models import Product
from faker import Faker
import json


class Command(BaseCommand):
    help = 'This command creates a list of users'

    def handle(self, *args, **options):
        faker = Faker()
        print('creamos el superuser')
        self.createSuperUser()
        print('Creamos empresa base')
        self.LoadBaseEnterprise()
        print('Fin')
        print('Cargamos Cuentas contables')
        self.loadCOAInEnterpise()
        print('cargamos cuenta de banco')
        self.createDefaultBank()
        print('cargamos proveedores')
        self.createPartners(faker)
        print('cargamos los productos')
        self.createProducts(faker)
        print('Fin')

    def createSuperUser(self):
        user = CustomUserModel.get('eduardouio7@gmail.com')
        if user:
            print('Ya existe el usuario')
            return True
        user = CustomUserModel(
            email='eduardouio7@gmail.com',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('seguro')
        user.save()

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
        # Obtener la compañía
        if Account.objects.filter(company__tax_id='9999999999').count() > 0:
            print('Ya existen cuentas')
            return True

        my_company = Company.get_by_tax_id('9999999999')
        if not my_company:
            raise Exception('No existe el cliente System Company')

        with open('common/accounts.JSON', 'r') as file:
            file_content = json.load(file)

        if file_content is None:
            raise Exception('No existe el archivo de cuentas')
        # Iterar sobre los niveles y crear las cuentas
        # Asegura que los niveles se procesen en orden
        for level in sorted(file_content.keys()):
            for account_data in file_content[level]:
                parent_account = None if level == 'level_1' else Account.get_account(
                    account_data['parent_account'], my_company
                )
                print('registramos {} {}'.format(level, account_data))
                Account.objects.create(
                    code=account_data['code'],
                    company=my_company,
                    name=account_data['name'],
                    type=account_data['type'],
                    level=account_data['level'],
                    is_children=account_data['is_children'],
                    description=account_data['description'],
                    parent_account=parent_account,
                    id_user_created=1
                )

    def createDefaultBank(self):
        my_company = Company.get_by_tax_id('9999999999')
        if not my_company:
            raise Exception('No existe el cliente System Company')

        my_account = Bank.get_by_account_number('0000000001', my_company)
        if my_account:
            print('Ya existe la cuenta')
            return True

        account = Account.get_account('1101003001', my_company)
        Bank.objects.create(
            account=account,
            name='Banco de prueba',
            account_number='0000000001',
            company=my_company,
            account_type='checking',
        )
        return True

    def createPartners(self, faker):
        my_company = Company.get_by_tax_id('9999999999')
        if not my_company:
            raise Exception('No existe el cliente System Company')

        suppliers = Partner.objects.filter(company=my_company, type='supplier')
        if suppliers.count() > 0:
            print('Ya existen proveedores')
            return True

        for _ in range(21):
            Partner.objects.create(
                company=my_company,
                name=faker.company(),
                id_num=faker.ean8(),
                email=faker.email(),
                type='supplier'
            )

        customers = Partner.objects.filter(company=my_company, type='customer')
        if customers.count() > 0:
            print('Ya existen clientes')
            return True

        for _ in range(36):
            Partner.objects.create(
                company=my_company,
                name=faker.company(),
                id_num=faker.ean8(),
                email=faker.email(),
                type='customer'
            )

    def createProducts(self, faker):
        my_company = Company.get_by_tax_id('9999999999')
        account = Account.get_account('1103001001', my_company)
        if not my_company:
            raise Exception('No existe el cliente System Company')

        products = Product.get_by_type('product', my_company)
        if len(products) > 0:
            print('Ya existen productos')
            return True

        for _ in range(76):
            Product.objects.create(
                company=my_company,
                account=account,
                code_sku=faker.ean13(),
                code_bars=faker.ean13(),
                name=faker.word(),
                price=faker.random_number(2),
                cost=faker.random_number(2),
                type='product'
            )

        services = Product.get_by_type('service', my_company)
        if len(services) > 0:
            print('Ya existen servicios')
            return True

        for _ in range(36):
            Product.objects.create(
                company=my_company,
                account=account,
                code_sku=faker.ean13(),
                code_bars=faker.ean13(),
                name=faker.word(),
                price=faker.random_number(2),
                cost=faker.random_number(2),
                type='service'
            )
        return True
