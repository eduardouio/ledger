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
class TestRetrieveViews:

    def setup_method(self):
        self.client = APIClient()

    def test_retrieve_account(self):
        account = Account.objects.create(name="Test Account")
        url = reverse('retrieve-account', args=[account.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Test Account"

    def test_retrieve_transaction(self):
        transaction = Transaction.objects.create(description="Test Transaction")
        url = reverse('retrieve-transaction', args=[transaction.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Test Transaction"

    def test_retrieve_general_ledger(self):
        general_ledger = GeneralLedger.objects.create(description="Test General Ledger")
        url = reverse('retrieve-general-ledger', args=[general_ledger.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Test General Ledger"

    def test_retrieve_company(self):
        company = Company.objects.create(name="Test Company")
        url = reverse('retrieve-company', args=[company.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Test Company"

    def test_retrieve_product(self):
        product = Product.objects.create(name="Test Product")
        url = reverse('retrieve-product', args=[product.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Test Product"

    def test_retrieve_inventory_movement(self):
        inventory_movement = InventoryMovement.objects.create(description="Test Movement")
        url = reverse('retrieve-inventory-movement', args=[inventory_movement.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Test Movement"

    def test_retrieve_partner(self):
        partner = Partner.objects.create(name="Test Partner")
        url = reverse('retrieve-partner', args=[partner.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Test Partner"

    def test_retrieve_invoice_items(self):
        invoice = Invoice.objects.create(number="INV123")
        invoice_item = InvoiceItems.objects.create(invoice=invoice, description="Test Item")
        url = reverse('retrieve-invoice-items', args=[invoice_item.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Test Item"

    def test_retrieve_invoice(self):
        invoice = Invoice.objects.create(number="INV123")
        url = reverse('retrieve-invoice', args=[invoice.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['number'] == "INV123"

    def test_retrieve_payment(self):
        payment = Payment.objects.create(amount=100)
        url = reverse('retrieve-payment', args=[payment.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['amount'] == 100

    def test_retrieve_warenhouse(self):
        warenhouse = Warenhouse.objects.create(name="Test Warenhouse")
        url = reverse('retrieve-warenhouse', args=[warenhouse.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Test Warenhouse"
