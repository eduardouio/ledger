from accounting.models import Account, Transaction, GeneralLedger
from companies.models import Company
from inventary.models import Product, InventoryMovement
from crm.models import Partner
from invoices.models import Invoice, Payment, InvoiceItems
from warenhouses.models import Warenhouse
from api.serializers import (AccountSerializer,
                             TransactionSerializer,
                             GeneralLedgerSerializer,
                             CompanySerializer,
                             ProductSerializer,
                             InventoryMovementSerializer,
                             PartnerSerializer,
                             InvoiceItemsSerializer,
                             InvoiceSerializer,
                             PaymentSerializer,
                             WarenhouseSerializer
                             )

from rest_framework.generics import UpdateAPIView


# /api/update/account/<int:pk>/
class UpdateAccountView(UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# /api/update/transaction/<int:pk>/
class UpdateTransactionView(UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# /api/update/general-ledger/<int:pk>/
class UpdateGeneralLedgerView(UpdateAPIView):
    queryset = GeneralLedger.objects.all()
    serializer_class = GeneralLedgerSerializer


# /api/update/company/<int:pk>/
class UpdateCompanyView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# /api/update/product/<int:pk>/
class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# /api/update/inventory-movement/<int:pk>/
class UpdateInventoryMovementView(UpdateAPIView):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer


# /api/update/partner/<int:pk>/
class UpdatePartnerView(UpdateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


# /api/update/invoice-items/<int:pk>/
class UpdateInvoiceItemsView(UpdateAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


# /api/update/invoice/<int:pk>/
class UpdateInvoiceView(UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


# /api/update/payment/<int:pk>/
class UpdatePaymentView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# /api/update/warenhouse/<int:pk>/
class UpdateWarenhouseView(UpdateAPIView):
    queryset = Warenhouse.objects.all()
    serializer_class = WarenhouseSerializer
