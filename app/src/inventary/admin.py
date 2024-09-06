from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from inventary.models import Product, InventoryMovement


class ProductAdmin(SimpleHistoryAdmin):
    list_display = (
        'name', 'company', 'code_bars',
        'code_sku', 'type', 'cost',
        'price'
    )


class InventoryMovementAdmin(SimpleHistoryAdmin):
    list_display = (
        'product', 'date', 'quantity',
        'warenhouse', 'movement',
        'user', 'total_cost'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(InventoryMovement, InventoryMovementAdmin)

