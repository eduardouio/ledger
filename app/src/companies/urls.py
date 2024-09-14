from django.urls import path
from .views import (
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
    CompanyListView,
    CompanyDetailView
)

urlpatterns = [
    path('company/create/', CompanyCreateView.as_view(), name='company-create'),
    path('company/<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company/', CompanyListView.as_view(), name='company-list'),
]
