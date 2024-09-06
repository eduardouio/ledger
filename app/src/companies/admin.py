from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from companies.models import Company


class CompanyAdmin(SimpleHistoryAdmin):
    list_display = (
        'name',
        'address',
        'email',
        'manager',
        'created_at',
        'is_active'
    )


admin.site.register(Company, CompanyAdmin)