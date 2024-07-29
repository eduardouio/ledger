from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from companies.models import Company


class CompanyAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Company, CompanyAdmin)