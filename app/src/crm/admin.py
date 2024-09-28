from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from crm.models import Partner


class ParentAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'type', 'company', 'id_num', 'email', 'pay_terms')
    search_fields = ['name', 'type']


admin.site.register(Partner, ParentAdmin)
