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

from rest_framework.generics import DestroyAPIView


# /api/delete/account/<int:pk>/
class DeleteAccountView(DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# /api/delete/transaction/<int:pk>/
class DeleteTransactionView(DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# /api/delete/general-ledger/<int:pk>/
class DeleteGeneralLedgerView(DestroyAPIView):
    queryset = GeneralLedger.objects.all()
    serializer_class = GeneralLedgerSerializer


# /api/delete/company/<int:pk>/
class DeleteCompanyView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# /api/delete/product/<int:pk>/
class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# /api/delete/inventory-movement/<int:pk>/
class DeleteInventoryMovementView(DestroyAPIView):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer


# /api/delete/partner/<int:pk>/
class DeletePartnerView(DestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


# /api/delete/invoice-items/<int:pk>/
class DeleteInvoiceItemsView(DestroyAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


# /api/delete/invoice/<int:pk>/
class DeleteInvoiceView(DestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


# /api/delete/payment/<int:pk>/
class DeletePaymentView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# /api/delete/warenhouse/<int:pk>/
class DeleteWarenhouseView(DestroyAPIView):
    queryset = Warenhouse.objects.all()
    serializer_class = WarenhouseSerializer
