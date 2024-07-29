from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from accounting.models import GeneralLedger, Transaction, Account


class GeneralLedgerAdmin(SimpleHistoryAdmin):
    pass


class TransactionAdmin(SimpleHistoryAdmin):
    pass


class AccountAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(GeneralLedger, GeneralLedgerAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)
