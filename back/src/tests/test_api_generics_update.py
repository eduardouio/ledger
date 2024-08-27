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
class TestUpdateViews:

    def setup_method(self):
        self.client = APIClient()

    def test_update_account(self):
        account = Account.objects.create(name="Old Account Name")
        url = reverse('update-account', args=[account.id])
        data = {'name': 'Updated Account Name'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Updated Account Name"

    def test_update_transaction(self):
        transaction = Transaction.objects.create(description="Old Transaction Description")
        url = reverse('update-transaction', args=[transaction.id])
        data = {'description': 'Updated Transaction Description'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Updated Transaction Description"

    def test_update_general_ledger(self):
        general_ledger = GeneralLedger.objects.create(description="Old General Ledger Description")
        url = reverse('update-general-ledger', args=[general_ledger.id])
        data = {'description': 'Updated General Ledger Description'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Updated General Ledger Description"

    def test_update_company(self):
        company = Company.objects.create(name="Old Company Name")
        url = reverse('update-company', args=[company.id])
        data = {'name': 'Updated Company Name'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Updated Company Name"

    def test_update_product(self):
        product = Product.objects.create(name="Old Product Name")
        url = reverse('update-product', args=[product.id])
        data = {'name': 'Updated Product Name'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Updated Product Name"

    def test_update_inventory_movement(self):
        inventory_movement = InventoryMovement.objects.create(description="Old Movement Description")
        url = reverse('update-inventory-movement', args=[inventory_movement.id])
        data = {'description': 'Updated Movement Description'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Updated Movement Description"

    def test_update_partner(self):
        partner = Partner.objects.create(name="Old Partner Name")
        url = reverse('update-partner', args=[partner.id])
        data = {'name': 'Updated Partner Name'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Updated Partner Name"

    def test_update_invoice_items(self):
        invoice = Invoice.objects.create(number="INV123")
        invoice_item = InvoiceItems.objects.create(invoice=invoice, description="Old Item Description")
        url = reverse('update-invoice-items', args=[invoice_item.id])
        data = {'description': 'Updated Item Description'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == "Updated Item Description"

    def test_update_invoice(self):
        invoice = Invoice.objects.create(number="INV123")
        url = reverse('update-invoice', args=[invoice.id])
        data = {'number': 'INV456'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['number'] == "INV456"

    def test_update_payment(self):
        payment = Payment.objects.create(amount=100)
        url = reverse('update-payment', args=[payment.id])
        data = {'amount': 200}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['amount'] == 200

    def test_update_warenhouse(self):
        warenhouse = Warenhouse.objects.create(name="Old Warenhouse Name")
        url = reverse('update-warenhouse', args=[warenhouse.id])
        data = {'name': 'Updated Warenhouse Name'}
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Updated Warenhouse Name"
