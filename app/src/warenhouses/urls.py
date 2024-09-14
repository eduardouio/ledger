from django.urls import path
from warenhouses.views import (
    WarenhouseCreateView,
    WarenhouseUpdateView,
    WarenhouseDeleteView,
    WarenhouseListView,
    WarenhouseDetailView
)

urlpatterns = [
    path('warenhouses/', WarenhouseListView.as_view(), name='warenhouse-list'),
    path('warenhouses/<int:pk>/', WarenhouseDetailView.as_view(), name='warenhouse-detail'),
    path('warenhouses/add/', WarenhouseCreateView.as_view(), name='warenhouse-create'),
    path('warenhouses/<int:pk>/edit/', WarenhouseUpdateView.as_view(), name='warenhouse-update'),
    path('warenhouses/<int:pk>/delete/', WarenhouseDeleteView.as_view(), name='warenhouse-delete'),
]
