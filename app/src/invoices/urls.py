from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    PaymentListView,
    PaymentDetailView,
    InvoiceCreateView,
    InvoiceDetailView,
    InvoiceListView,
    InvoiceDeleteView,
    BillCreateView,
    BillDetailView,
    BillDeleteView,
    BillListView
)

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/add/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/edit/<int:pk>/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/delete/<int:pk>/', PaymentDeleteView.as_view(), name='payment-delete'),

    path('bills/create/', BillCreateView.as_view(), name='bills-create'),
    path('bills/delete/<int:pk>/', BillDeleteView.as_view(), name='bills-delete'),
    path('bills/<int:pk>/', BillDetailView.as_view(), name='bills-detail'),
    path('bills/', BillListView.as_view(), name='bills-list'),

    path('sales/create/', InvoiceCreateView.as_view(), name='sales-create'),
    path('sales/delete/<int:pk>/', InvoiceDeleteView.as_view(), name='sales-delete'),
    path('sales/<int:pk>/', InvoiceDetailView.as_view(), name='sales-detail'),
    path('sales/', InvoiceListView.as_view(), name='sales-list'),
]
