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
class TestListViews:

    def setup_method(self):
        self.client = APIClient()

    def test_list_account(self):
        Account.objects.create(name="Account 1")
        Account.objects.create(name="Account 2")
        url = reverse('list-account')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['name'] == "Account 1"
        assert response.data[1]['name'] == "Account 2"

    def test_list_transaction(self):
        Transaction.objects.create(description="Transaction 1")
        Transaction.objects.create(description="Transaction 2")
        url = reverse('list-transaction')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['description'] == "Transaction 1"
        assert response.data[1]['description'] == "Transaction 2"

    def test_list_general_ledger(self):
        GeneralLedger.objects.create(description="General Ledger 1")
        GeneralLedger.objects.create(description="General Ledger 2")
        url = reverse('list-general-ledger')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['description'] == "General Ledger 1"
        assert response.data[1]['description'] == "General Ledger 2"

    def test_list_company(self):
        Company.objects.create(name="Company 1")
        Company.objects.create(name="Company 2")
        url = reverse('list-company')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['name'] == "Company 1"
        assert response.data[1]['name'] == "Company 2"

    def test_list_product(self):
        Product.objects.create(name="Product 1")
        Product.objects.create(name="Product 2")
        url = reverse('list-product')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['name'] == "Product 1"
        assert response.data[1]['name'] == "Product 2"

    def test_list_inventory_movement(self):
        InventoryMovement.objects.create(description="Movement 1")
        InventoryMovement.objects.create(description="Movement 2")
        url = reverse('list-inventory-movement')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['description'] == "Movement 1"
        assert response.data[1]['description'] == "Movement 2"

    def test_list_partner(self):
        Partner.objects.create(name="Partner 1")
        Partner.objects.create(name="Partner 2")
        url = reverse('list-partner')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['name'] == "Partner 1"
        assert response.data[1]['name'] == "Partner 2"

    def test_list_invoice_items(self):
        invoice = Invoice.objects.create(number="INV123")
        InvoiceItems.objects.create(invoice=invoice, description="Item 1")
        InvoiceItems.objects.create(invoice=invoice, description="Item 2")
        url = reverse('list-invoice-items')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['description'] == "Item 1"
        assert response.data[1]['description'] == "Item 2"

    def test_list_invoice(self):
        Invoice.objects.create(number="INV123")
        Invoice.objects.create(number="INV456")
        url = reverse('list-invoice')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['number'] == "INV123"
        assert response.data[1]['number'] == "INV456"

    def test_list_payment(self):
        Payment.objects.create(amount=100)
        Payment.objects.create(amount=200)
        url = reverse('list-payment')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['amount'] == 100
        assert response.data[1]['amount'] == 200

    def test_list_warenhouse(self):
        Warenhouse.objects.create(name="Warenhouse 1")
        Warenhouse.objects.create(name="Warenhouse 2")
        url = reverse('list-warenhouse')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['name'] == "Warenhouse 1"
        assert response.data[1]['name'] == "Warenhouse 2"
