from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from accounting.models import Bank
from accounting.forms import BankForm
from companies.models import Company


class BankCreateView(LoginRequiredMixin, CreateView):
    model = Bank
    form_class = BankForm
    template_name = 'bank/bank-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(BankCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Bank Account'
        ctx['company'] = Company.get_by_user(self.request.user)
        return ctx

    def get_success_url(self):
        url = reverse_lazy('bank-detail', kwargs={'pk': self.object.pk})
        url = f'{url}?action=created'
        return url


class BankUpdateView(LoginRequiredMixin, UpdateView):
    model = Bank
    form_class = BankForm
    template_name = 'bank/bank-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(BankUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Bank Account'
        return ctx

    def get_success_url(self):
        url = reverse_lazy('bank-detail', kwargs={'pk': self.object.pk})
        url = f'{url}?action=updated'
        return url


class BankDeleteView(LoginRequiredMixin, DeleteView):
    model = Bank
    success_url = reverse_lazy('bank-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        bank = self.get_object()
        if bank.company != Company.get_by_user(request.user):
            raise Exception('Error deleting bank')

        bank.delete()
        return HttpResponseRedirect(self.success_url + '?action=deleted')


class BankListView(LoginRequiredMixin, ListView):
    model = Bank
    template_name = 'bank/bank-list.html'
    context_object_name = 'banks'

    def get_queryset(self):
        my_company = Company.get_by_user(self.request.user)
        if not my_company:
            raise ValueError('No company found for the current user')

        return Bank.get_accounts(my_company)

    def get_context_data(self, **kwargs):
        ctx = super(BankListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Bank Accounts List'
        ctx['create_url'] = reverse_lazy('bank-create')
        ctx['company'] = Company.get_by_user(self.request.user)
        ctx['action_type'] = None
        ctx['module_name'] = 'banks'
        ctx['url_new'] = reverse_lazy('bank-create')

        if self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Bank deleted succesfully'
        return ctx


class BankDetailView(LoginRequiredMixin, DetailView):
    model = Bank
    template_name = 'bank/bank-presentation.html'
    context_object_name = 'bank'

    def get_context_data(self, **kwargs):
        ctx = super(BankDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Bank Account Detail'
        ctx['action_type'] = None

        if self.request.GET.get('action') == 'updated':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Bank updated successfully'
        if self.request.GET.get('action') == 'created':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Bank updated successfully'
        if self.request.GET.get('action') == 'alert':
            ctx['action_type'] = 'alert'
            ctx['message'] = 'The Bank will be removed, cannot be undone.'

        return ctx
