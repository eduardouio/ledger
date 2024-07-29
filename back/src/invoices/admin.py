from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from invoices.models import Invoice, Payment, InvoiceItems


class InvoiceAdmin(SimpleHistoryAdmin):
    pass


class InvoiceLineAdmin(SimpleHistoryAdmin):
    pass


class PaymentAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(InvoiceItems, InvoiceLineAdmin)
