from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from inventary.models import Product, InventoryMovement


class ProductAdmin(SimpleHistoryAdmin):
    pass


class InventoryMovementAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(InventoryMovement, InventoryMovementAdmin)
