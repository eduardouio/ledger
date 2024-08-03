from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from warenhouses.models import Warenhouse


class WarenhouseAdmin(SimpleHistoryAdmin):
    list_display = (
        'company',
        'code',
        'name',
        'address',
        'created_at',
        'is_active'
    )


admin.site.register(Warenhouse, WarenhouseAdmin)
