from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from accounting.models import Account
from accounting.forms import AccountForm


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'account_form.html'
    success_url = reverse_lazy('account-list')


class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'account_form.html'
    success_url = reverse_lazy('account-list')


class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'account_confirm_delete.html'
    success_url = reverse_lazy('account-list')


class ListAccountsView(ListView):
    model = Account
    template_name = 'account_list.html'
    context_object_name = 'accounts'
    paginate_by = 10
    queryset = Account.objects.all()