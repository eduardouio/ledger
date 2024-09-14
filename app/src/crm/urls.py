from django.urls import path
from .views import (
    PartnerCreateView,
    PartnerUpdateView,
    PartnerDeleteView,
    PartnerListView,
    PartnerDetailView
)

urlpatterns = [
    path('partners/', PartnerListView.as_view(), name='partner-list'),
    path('partners/<int:pk>/', PartnerDetailView.as_view(), name='partner-detail'),
    path('partners/add/', PartnerCreateView.as_view(), name='partner-create'),
    path('partners/<int:pk>/edit/', PartnerUpdateView.as_view(), name='partner-update'),
    path('partners/<int:pk>/delete/', PartnerDeleteView.as_view(), name='partner-delete'),
]
