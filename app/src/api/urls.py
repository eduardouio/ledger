from django.urls import path
from api.views.generics.DeleteViews import (
    DeleteAccountView,
    DeleteTransactionView,
    DeleteGeneralLedgerView,
    DeleteCompanyView,
    DeleteProductView,
    DeleteInventoryMovementView,
    DeletePartnerView,
    DeleteInvoiceItemsView,
    DeleteInvoiceView,
    DeletePaymentView,
    DeleteWarenhouseView
)
from api.views.generics.ListViews import (
    ListAccountView,
    ListTransactionView,
    ListGeneralLedgerView,
    ListCompanyView,
    ListProductView,
    ListInventoryMovementView,
    ListPartnerView,
    ListInvoiceItemsView,
    ListInvoiceView,
    ListPaymentView,
    ListWarenhouseView
)
from api.views.generics.RetrieveViews import (
    RetrieveAccountView,
    RetrieveTransactionView,
    RetrieveGeneralLedgerView,
    RetrieveCompanyView,
    RetrieveProductView,
    RetrieveInventoryMovementView,
    RetrievePartnerView,
    RetrieveInvoiceItemsView,
    RetrieveInvoiceView,
    RetrievePaymentView,
    RetrieveWarenhouseView
)
from api.views.generics.UpdateViews import (
    UpdateAccountView,
    UpdateTransactionView,
    UpdateGeneralLedgerView,
    UpdateCompanyView,
    UpdateProductView,
    UpdateInventoryMovementView,
    UpdatePartnerView,
    UpdateInvoiceItemsView,
    UpdateInvoiceView,
    UpdatePaymentView,
    UpdateWarenhouseView
)


urlpatterns = [
    # Account URLs
    path('gn/list/account/', ListAccountView.as_view(), name='list-account'),
    path('gn/detail/account/<int:pk>/', RetrieveAccountView.as_view(), name='retrieve-account'),
    path('gn/update/account/<int:pk>/', UpdateAccountView.as_view(), name='update-account'),
    path('gn/delete/account/<int:pk>/', DeleteAccountView.as_view(), name='delete-account'),

    # Transaction URLs
    path('gn/list/transaction/', ListTransactionView.as_view(), name='list-transaction'),
    path('gn/detail/transaction/<int:pk>/', RetrieveTransactionView.as_view(), name='retrieve-transaction'),
    path('gn/update/transaction/<int:pk>/', UpdateTransactionView.as_view(), name='update-transaction'),
    path('gn/delete/transaction/<int:pk>/', DeleteTransactionView.as_view(), name='delete-transaction'),

    # General Ledger URLs
    path('gn/list/general-ledger/', ListGeneralLedgerView.as_view(), name='list-general-ledger'),
    path('gn/detail/general-ledger/<int:pk>/', RetrieveGeneralLedgerView.as_view(), name='retrieve-general-ledger'),
    path('gn/update/general-ledger/<int:pk>/', UpdateGeneralLedgerView.as_view(), name='update-general-ledger'),
    path('gn/delete/general-ledger/<int:pk>/', DeleteGeneralLedgerView.as_view(), name='delete-general-ledger'),

    # Company URLs
    path('gn/list/company/', ListCompanyView.as_view(), name='list-company'),
    path('gn/detail/company/<int:pk>/', RetrieveCompanyView.as_view(), name='retrieve-company'),
    path('gn/update/company/<int:pk>/', UpdateCompanyView.as_view(), name='update-company'),
    path('gn/delete/company/<int:pk>/', DeleteCompanyView.as_view(), name='delete-company'),

    # Product URLs
    path('gn/list/product/', ListProductView.as_view(), name='list-product'),
    path('gn/detail/product/<int:pk>/', RetrieveProductView.as_view(), name='retrieve-product'),
    path('gn/update/product/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    path('gn/delete/product/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),

    # Inventory Movement URLs
    path('gn/list/inventory-movement/', ListInventoryMovementView.as_view(), name='list-inventory-movement'),
    path('gn/detail/inventory-movement/<int:pk>/', RetrieveInventoryMovementView.as_view(), name='retrieve-inventory-movement'),
    path('gn/update/inventory-movement/<int:pk>/', UpdateInventoryMovementView.as_view(), name='update-inventory-movement'),
    path('gn/delete/inventory-movement/<int:pk>/', DeleteInventoryMovementView.as_view(), name='delete-inventory-movement'),

    # Partner URLs
    path('gn/list/partner/', ListPartnerView.as_view(), name='list-partner'),
    path('gn/detail/partner/<int:pk>/', RetrievePartnerView.as_view(), name='retrieve-partner'),
    path('gn/update/partner/<int:pk>/', UpdatePartnerView.as_view(), name='update-partner'),
    path('gn/delete/partner/<int:pk>/', DeletePartnerView.as_view(), name='delete-partner'),

    # Invoice Items URLs
    path('gn/list/invoice-items/', ListInvoiceItemsView.as_view(), name='list-invoice-items'),
    path('gn/detail/invoice-items/<int:pk>/', RetrieveInvoiceItemsView.as_view(), name='retrieve-invoice-items'),
    path('gn/update/invoice-items/<int:pk>/', UpdateInvoiceItemsView.as_view(), name='update-invoice-items'),
    path('gn/delete/invoice-items/<int:pk>/', DeleteInvoiceItemsView.as_view(), name='delete-invoice-items'),

    # Invoice URLs
    path('gn/list/invoice/', ListInvoiceView.as_view(), name='list-invoice'),
    path('gn/detail/invoice/<int:pk>/', RetrieveInvoiceView.as_view(), name='retrieve-invoice'),
    path('gn/update/invoice/<int:pk>/', UpdateInvoiceView.as_view(), name='update-invoice'),
    path('gn/delete/invoice/<int:pk>/', DeleteInvoiceView.as_view(), name='delete-invoice'),

    # Payment URLs
    path('gn/list/payment/', ListPaymentView.as_view(), name='list-payment'),
    path('gn/detail/payment/<int:pk>/', RetrievePaymentView.as_view(), name='retrieve-payment'),
    path('gn/update/payment/<int:pk>/', UpdatePaymentView.as_view(), name='update-payment'),
    path('gn/delete/payment/<int:pk>/', DeletePaymentView.as_view(), name='delete-payment'),

    # Warenhouse URLs
    path('gn/list/warenhouse/', ListWarenhouseView.as_view(), name='list-warenhouse'),
    path('gn/detail/warenhouse/<int:pk>/', RetrieveWarenhouseView.as_view(), name='retrieve-warenhouse'),
    path('gn/update/warenhouse/<int:pk>/', UpdateWarenhouseView.as_view(), name='update-warenhouse'),
    path('gn/delete/warenhouse/<int:pk>/', DeleteWarenhouseView.as_view(), name='delete-warenhouse'),
]
