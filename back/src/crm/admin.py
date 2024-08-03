from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from crm.models import Supplier, Customer


class SupplierAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'company',)


class CustomerAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'company',)


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
