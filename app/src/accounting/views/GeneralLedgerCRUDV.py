from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from accounting.models import GeneralLedger
from accounting.forms import GeneralLedgerForm
from companies.models import Company


class GeneralLedgerCreateView(CreateView):
    model = GeneralLedger
    form_class = GeneralLedgerForm
    template_name = 'generalledger/generalledger_form.html'
    success_url = reverse_lazy('generalledger-list')

    def get_context_data(self, **kwargs):
        ctx = super(GeneralLedgerCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create General Ledger Entry'
        return ctx


class GeneralLedgerUpdateView(UpdateView):
    model = GeneralLedger
    form_class = GeneralLedgerForm
    template_name = 'generalledger/generalledger-form.html'
    success_url = reverse_lazy('generalledger-list')

    def get_context_data(self, **kwargs):
        ctx = super(GeneralLedgerUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update General Ledger Entry'
        return ctx


class GeneralLedgerDeleteView(DeleteView):
    model = GeneralLedger
    template_name = 'generalledger/generalledger-confirm-delete.html'
    success_url = reverse_lazy('generalledger-list')

    def get_context_data(self, **kwargs):
        ctx = super(GeneralLedgerDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete General Ledger Entry'
        return ctx


class GeneralLedgerListView(ListView):
    model = GeneralLedger
    template_name = 'generalledger/generalledger-list.html'
    context_object_name = 'ledgers'

    def get_queryset(self):
                # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return GeneralLedger.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return GeneralLedger.getLedgersByAccount(self.request.user.account, my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(GeneralLedgerListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'General Ledger Entries List'
        return ctx


class GeneralLedgerDetailView(DetailView):
    model = GeneralLedger
    template_name = 'generalledger/generalledger-presentation.html'
    context_object_name = 'generalledger'

    def get_context_data(self, **kwargs):
        ctx = super(GeneralLedgerDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'General Ledger Detail'
        return ctx