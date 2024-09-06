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

from rest_framework.generics import ListAPIView


# /api/list/account/
class ListAccountView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# /api/list/transaction/
class ListTransactionView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# /api/list/general-ledger/
class ListGeneralLedgerView(ListAPIView):
    queryset = GeneralLedger.objects.all()
    serializer_class = GeneralLedgerSerializer


# /api/list/company/
class ListCompanyView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# /api/list/product/
class ListProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# /api/list/inventory-movement/
class ListInventoryMovementView(ListAPIView):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer


# /api/list/partner/
class ListPartnerView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


# /api/list/invoice-items/
class ListInvoiceItemsView(ListAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


# /api/list/invoice/
class ListInvoiceView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


# /api/list/payment/
class ListPaymentView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# /api/list/warenhouse/
class ListWarenhouseView(ListAPIView):
    queryset = Warenhouse.objects.all()
    serializer_class = WarenhouseSerializer
