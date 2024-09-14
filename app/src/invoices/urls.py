from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentUpdateView,
    PaymentDeleteView,
    PaymentListView,
    PaymentDetailView
)

urlpatterns = [
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/add/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/edit/', PaymentUpdateView.as_view(), name='payment-update'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),
]
