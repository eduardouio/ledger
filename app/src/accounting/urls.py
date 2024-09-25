from django.urls import path
from .views import (
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    AccountListView,
    AccountDetailView,
    BankCreateView,BankUpdateView,BankDeleteView,BankListView,BankDetailView,
    TransactionCreateView,TransactionUpdateView,TransactionDeleteView,TransactionListView,TransactionDetailView,
    GeneralLedgerCreateView,GeneralLedgerUpdateView,GeneralLedgerDeleteView,GeneralLedgerListView,GeneralLedgerDetailView
)

urlpatterns = [
    path('account/', AccountListView.as_view(), name='account-list'),
    path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('account/new/', AccountCreateView.as_view(), name='account-create'),
    path('account/<int:pk>/edit/', AccountUpdateView.as_view(), name='account-update'),
    path('account/<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),

    path('transaction/new/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transaction/', TransactionListView.as_view(), name='transaction-list'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),

    path('generalledger/new/', GeneralLedgerCreateView.as_view(), name='generalledger-create'),
    path('generalledger/<int:pk>/edit/', GeneralLedgerUpdateView.as_view(), name='generalledger-update'),
    path('generalledger/<int:pk>/delete/', GeneralLedgerDeleteView.as_view(), name='generalledger-delete'),
    path('generalledger/', GeneralLedgerListView.as_view(), name='generalledger-list'),
    path('generalledger/<int:pk>/', GeneralLedgerDetailView.as_view(), name='generalledger-detail'),

    path('banks/new/', BankCreateView.as_view(), name='bank-create'),
    path('banks/<int:pk>/edit/', BankUpdateView.as_view(), name='bank-update'),
    path('banks/<int:pk>/delete/', BankDeleteView.as_view(), name='bank-delete'),
    path('banks/', BankListView.as_view(), name='bank-list'),
    path('banks/<int:pk>/', BankDetailView.as_view(), name='bank-detail'),
]
