from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from invoices.models import Invoice, Payment, InvoiceItems


class InvoiceLineAdmin(admin.TabularInline):
    model = InvoiceItems
    extra = 1


class InvoiceAdmin(SimpleHistoryAdmin):
    list_display = (
        'id','number', 'company', 'date',
        'due_date', 'amount', 'tax',
        'user', 'status'
        )
    inlines = [InvoiceLineAdmin]


class PaymentAdmin(SimpleHistoryAdmin):
    list_display = ('date', 'amount', 'method')


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Payment, PaymentAdmin)
