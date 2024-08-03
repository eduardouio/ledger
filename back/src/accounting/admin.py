from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from accounting.models import GeneralLedger, Transaction, Account


class GeneralLedgerAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'company', 'account', 'balance', 'created_at')


class TransactionAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'company', 'account', 'amount', 'date', 'user')


class AccountAdmin(SimpleHistoryAdmin):
    list_display = ('code', 'name', 'type', 'company')


admin.site.register(GeneralLedger, GeneralLedgerAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)
