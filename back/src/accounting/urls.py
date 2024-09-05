from django.urls import path
from .views import (
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    AccountListView,
    AccountDetailView
)

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('account/new/', AccountCreateView.as_view(), name='account-create'),
    path('account/<int:pk>/edit/', AccountUpdateView.as_view(), name='account-update'),
    path('account/<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),

]
