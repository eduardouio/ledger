from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from accounting.models import Transaction
from accounting.forms import TransactionForm
from companies.models import Company


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/transaction-form.html'
    success_url = reverse_lazy('transaction-list')

    def get_context_data(self, **kwargs):
        ctx = super(TransactionCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Transaction'
        return ctx


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/transaction-form.html'
    success_url = reverse_lazy('transaction-list')

    def get_context_data(self, **kwargs):
        ctx = super(TransactionUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Transaction'
        return ctx


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transaction/transaction-confirm-delete.html'
    success_url = reverse_lazy('transaction-list')

    def get_context_data(self, **kwargs):
        ctx = super(TransactionDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Transaction'
        return ctx


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction-list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
                # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return Transaction.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Transaction.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(TransactionListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Transaction List'
        return ctx


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction/transaction-presentation.html'
    context_object_name = 'transaction'

    def get_context_data(self, **kwargs):
        ctx = super(TransactionDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Transaction Detail'
        return ctx
