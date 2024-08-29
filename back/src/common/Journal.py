from datetime import date
from accounting.models import Transaction, GeneralLedger, Account
from invoices.models import InvoiceItems


class Journal(object):

    def purcharseOrderInventary(self, invoice):
        company = invoice.company
        accout_inventary = Account.get_account('1103001001', company)
        account_payable = Account.get_account('2102001001', company)
        taxes_payable = Account.get_account('2103001001', company)

        invoice = InvoiceItems.get_by_id(invoice)
        my_trasanction = Transaction(
            company=company,
            description='Purchase Order Inventary',
            amount=invoice.amount,
            date=date.today(),
            user=invoice.user
        )
        my_trasanction.save()
        GeneralLedger.objects.create(
            company=company,
            account=accout_inventary,
            transaction=my_trasanction,
            debit=invoice.amount,
            credit=0,
            balance=invoice.amount,
            description='Purchase Order Inventary'
        )
        GeneralLedger.objects.create(
            company=company,
            account=account_payable,
            transaction=my_trasanction,
            debit=0,
            credit=invoice.amount,
            balance=invoice.amount,
            description='Payable Order Inventary'
        )
        GeneralLedger.objects.create(
            company=company,
            account=taxes_payable,
            transaction=my_trasanction,
            debit=0,
            credit=invoice.tax,
            balance=invoice.tax,
            description='Purchase Order Inventary'
        )