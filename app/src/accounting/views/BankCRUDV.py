from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from ..models import Bank
from ..forms import BankForm
from companies.models import Company


class BankCreateView(CreateView):
    model = Bank
    form_class = BankForm
    template_name = 'bank/bank-form.html'
    success_url = reverse_lazy('bank-list')

    def get_context_data(self, **kwargs):
        ctx = super(BankCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Bank Account'
        return ctx


class BankUpdateView(UpdateView):
    model = Bank
    form_class = BankForm
    template_name = 'bank/bank-form.html'
    success_url = reverse_lazy('bank-list')

    def get_context_data(self, **kwargs):
        ctx = super(BankUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Bank Account'
        return ctx


class BankDeleteView(DeleteView):
    model = Bank
    template_name = 'bank/bank-confirm-delete.html'
    success_url = reverse_lazy('bank-list')

    def get_context_data(self, **kwargs):
        ctx = super(BankDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Bank Account'
        return ctx


class BankListView(ListView):
    model = Bank
    template_name = 'bank/bank-list.html'
    context_object_name = 'banks'

    def get_queryset(self):
        # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return Bank.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Bank.get_accounts(my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(BankListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Bank Accounts List'
        return ctx


class BankDetailView(DetailView):
    model = Bank
    template_name = 'bank/bank_presentation.html'
    context_object_name = 'bank'

    def get_context_data(self, **kwargs):
        ctx = super(BankDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Bank Account Detail'
        return ctx
