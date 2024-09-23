from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from accounting.models import Account
from accounting.forms import AccountForm
from companies.models import Company


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounting/account_form.html'

    def get_context_data(self, **kwargs):
        ctx = super(AccountCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Account'
        ctx['company'] = Company.get_by_user(self.request.user)
        return ctx

    def get_success_url(self):
        url = reverse_lazy('account-detail', kwargs={'pk': self.object.id})
        url += '?action=created'
        return url


# /accounting/account/<pk>/edit/
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounting/account_form.html'

    def get_context_data(self, **kwargs):
        ctx = super(AccountUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Account'
        return ctx

    def get_success_url(self):
        url = reverse_lazy('account-detail', kwargs={'pk': self.object.id})
        url += '?action=updated'
        return url


# /accounting/delete/pk/
class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('account-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        account = self.get_object()
        if account.company != Company.get_by_user(request.user):
            return HttpResponseRedirect

        account.delete()
        return HttpResponseRedirect(self.success_url + '?action=deleted')


# /accounting/
class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'accounting/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Account.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Account.get_accounts(my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(AccountListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Accounts List'
        ctx['action_type'] = None
        ctx['module_name'] = 'accounts'
        ctx['url_new'] = reverse_lazy('account-create')

        if self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Account deleted successfully'

        return ctx


# /accounting/account/<pk>/
class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'accounting/account_presentation.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        ctx = super(AccountDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Account Detail'
        ctx['action_type'] = None
        if self.request.GET.get('action') == 'updated':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Account updated successfully'
        elif self.request.GET.get('action') == 'created':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Account created successfully'
        elif self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Account deleted successfully'
        elif self.request.GET.get('action') == 'alert':
            ctx['action_type'] = 'alert'
            ctx['message'] = 'The Partner will be removed, cannot be undone.'
        return ctx
