from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    PaymentListView,
    PaymentDetailView,
    InvoiceCreateView,
    InvoiceUpdateView,
    InvoiceDetailView,
    InvoiceListView,
    InvoiceDeleteView
)

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/add/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/edit/<int:pk>/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/delete/<int:pk>/', PaymentDeleteView.as_view(), name='payment-delete'),

    path('bills/create/', InvoiceCreateView.as_view(), name='bills-create'),
    path('bills/update/<int:pk>/', InvoiceUpdateView.as_view(), name='bills-update'),
    path('bills/delete/<int:pk>/', InvoiceDeleteView.as_view(), name='bills-delete'),
    path('bills/<int:pk>/', InvoiceDetailView.as_view(), name='bills-detail'),
    path('bills/', InvoiceListView.as_view(), name='bills-list'),

    path('invoices/create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoices/update/<int:pk>/', InvoiceUpdateView.as_view(), name='invoice-update'),
    path('invoices/delete/<int:pk>/', InvoiceDeleteView.as_view(), name='invoice-delete'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoices/', InvoiceListView.as_view(), name='invoice-list'),
]
