from django.urls import path
from .views import AccountCreateView, AccountUpdateView, AccountDeleteView

urlpatterns = [
    path('account/new/', AccountCreateView.as_view(), name='account-create'),
    path('account/<int:pk>/edit/', AccountUpdateView.as_view(), name='account-update'),
    path('account/<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),
]
