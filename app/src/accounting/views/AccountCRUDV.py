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

    def get_context_data(self, **kwargs):
        ctx = super(AccountCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Account'
        return ctx


# /accounting/account/<pk>/edit/
class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounting/account_form.html'
    success_url = reverse_lazy('account-list')

    def get_context_data(self, **kwargs):
        ctx = super(AccountUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Account'
        return ctx


# /accounting/delete/pk/
class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'accounting/account_confirm_delete.html'
    success_url = reverse_lazy('account-list')

    def get_context_data(self, **kwargs):
        ctx = super(AccountDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Account'
        return ctx


# /accounting/
class AccountListView(ListView):
    model = Account
    template_name = 'accounting/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Account.get_accounts(my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(AccountListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Accounts List'
        return ctx


# /accounting/account/<pk>/
class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounting/account_presentation.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        ctx = super(AccountDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Account Detail'
        return ctx
