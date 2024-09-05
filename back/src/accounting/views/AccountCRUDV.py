from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from accounting.models import Account
from accounting.forms import AccountForm
from companies.models import Company


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounting/account_form.html'
    success_url = reverse_lazy('account-list')


class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounting/account_form.html'
    success_url = reverse_lazy('account-list')


class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'accounting/account_confirm_delete.html'
    success_url = reverse_lazy('account-list')


class AccountListView(ListView):
    model = Account
    template_name = 'accounting/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Account.get_accounts(my_company)
        return []


class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounting/account_detail.html'
    context_object_name = 'account'
    paginate_by = 10
    queryset = Account.objects.all()
