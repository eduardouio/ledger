from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from crm.models import Supplier, Customer


class SupplierAdmin(SimpleHistoryAdmin):
    pass


class CustomerAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
