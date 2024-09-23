from django.urls import path
from .views import (
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
    CompanyListView,
    CompanyDetailView
)

urlpatterns = [
    path('companies/<int:pk>/edit/', CompanyUpdateView.as_view(), name='company-update'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
]
