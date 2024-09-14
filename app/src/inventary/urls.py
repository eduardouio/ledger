from django.urls import path
from .views import (
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView,
    ProductDetailView,
    InventoryMovementCreateView,InventoryMovementUpdateView,InventoryMovementDeleteView,InventoryMovementListView,InventoryMovementDetailView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/add/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    
    path('inventory-movements/', InventoryMovementListView.as_view(), name='inventorymovement-list'),
    path('inventory-movements/<int:pk>/', InventoryMovementDetailView.as_view(), name='inventorymovement-detail'),
    path('inventory-movements/add/', InventoryMovementCreateView.as_view(), name='inventorymovement-create'),
    path('inventory-movements/<int:pk>/edit/', InventoryMovementUpdateView.as_view(), name='inventorymovement-update'),
    path('inventory-movements/<int:pk>/delete/', InventoryMovementDeleteView.as_view(), name='inventorymovement-delete'),
]
