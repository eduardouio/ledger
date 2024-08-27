import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounting.models import Account, Transaction, GeneralLedger
from companies.models import Company
from inventary.models import Product, InventoryMovement
from crm.models import Partner
from invoices.models import Invoice, Payment, InvoiceItems
from warenhouses.models import Warenhouse

@pytest.mark.django_db
class TestDeleteViews:

    def setup_method(self):
        self.client = APIClient()

    def test_delete_account(self):
        account = Account.objects.create(name="Test Account")
        url = reverse('delete-account', args=[account.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Account.objects.filter(id=account.id).count() == 0

    def test_delete_transaction(self):
        transaction = Transaction.objects.create(description="Test Transaction")
        url = reverse('delete-transaction', args=[transaction.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Transaction.objects.filter(id=transaction.id).count() == 0

    def test_delete_general_ledger(self):
        general_ledger = GeneralLedger.objects.create(description="Test General Ledger")
        url = reverse('delete-general-ledger', args=[general_ledger.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert GeneralLedger.objects.filter(id=general_ledger.id).count() == 0

    def test_delete_company(self):
        company = Company.objects.create(name="Test Company")
        url = reverse('delete-company', args=[company.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Company.objects.filter(id=company.id).count() == 0

    def test_delete_product(self):
        product = Product.objects.create(name="Test Product")
        url = reverse('delete-product', args=[product.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Product.objects.filter(id=product.id).count() == 0

    def test_delete_inventory_movement(self):
        inventory_movement = InventoryMovement.objects.create(description="Test Movement")
        url = reverse('delete-inventory-movement', args=[inventory_movement.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert InventoryMovement.objects.filter(id=inventory_movement.id).count() == 0

    def test_delete_partner(self):
        partner = Partner.objects.create(name="Test Partner")
        url = reverse('delete-partner', args=[partner.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Partner.objects.filter(id=partner.id).count() == 0

    def test_delete_invoice_items(self):
        invoice = Invoice.objects.create(number="INV123")
        invoice_item = InvoiceItems.objects.create(invoice=invoice, description="Test Item")
        url = reverse('delete-invoice-items', args=[invoice_item.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert InvoiceItems.objects.filter(id=invoice_item.id).count() == 0

    def test_delete_invoice(self):
        invoice = Invoice.objects.create(number="INV123")
        url = reverse('delete-invoice', args=[invoice.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Invoice.objects.filter(id=invoice.id).count() == 0

    def test_delete_payment(self):
        payment = Payment.objects.create(amount=100)
        url = reverse('delete-payment', args=[payment.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Payment.objects.filter(id=payment.id).count() == 0

    def test_delete_warenhouse(self):
        warenhouse = Warenhouse.objects.create(name="Test Warenhouse")
        url = reverse('delete-warenhouse', args=[warenhouse.id])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Warenhouse.objects.filter(id=warenhouse.id).count() == 0
