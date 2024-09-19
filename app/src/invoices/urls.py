from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    PaymentListView,
    PaymentDetailView,
    InvoiceCreateView, InvoiceUpdateView,InvoiceDetailView,InvoiceListView, InvoiceDeleteView
)

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/add/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/edit/<int:pk>/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/delete/<int:pk>/', PaymentDeleteView.as_view(), name='payment-delete'),
    
    path('invoice/create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoice/update/<int:pk>/', InvoiceUpdateView.as_view(), name='invoice-update'),
    path('invoice/delete/<int:pk>/', InvoiceDeleteView.as_view(), name='invoice-delete'),
    path('invoice/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice/', InvoiceListView.as_view(), name='invoice-list'),
]
