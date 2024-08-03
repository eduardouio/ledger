from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'This command creates a list of users'

    def handle(self, *args, **options):
        print('Cargamos las cuentas contables')

    def loadCOA(self):
        