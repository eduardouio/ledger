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

from rest_framework.generics import RetrieveAPIView


# /api/detail/account/<int:pk>/
class RetrieveAccountView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# /api/detail/transaction/<int:pk>/
class RetrieveTransactionView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# /api/detail/general-ledger/<int:pk>/
class RetrieveGeneralLedgerView(RetrieveAPIView):
    queryset = GeneralLedger.objects.all()
    serializer_class = GeneralLedgerSerializer


# /api/detail/company/<int:pk>/
class RetrieveCompanyView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# /api/detail/product/<int:pk>/
class RetrieveProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# /api/detail/inventory-movement/<int:pk>/
class RetrieveInventoryMovementView(RetrieveAPIView):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer


# /api/detail/partner/<int:pk>/
class RetrievePartnerView(RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


# /api/detail/invoice-items/<int:pk>/
class RetrieveInvoiceItemsView(RetrieveAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


# /api/detail/invoice/<int:pk>/
class RetrieveInvoiceView(RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


# /api/detail/payment/<int:pk>/
class RetrievePaymentView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# /api/detail/warenhouse/<int:pk>/
class RetrieveWarenhouseView(RetrieveAPIView):
    queryset = Warenhouse.objects.all()
    serializer_class = WarenhouseSerializer
