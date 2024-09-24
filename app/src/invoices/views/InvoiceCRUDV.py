from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from django.forms.models import inlineformset_factory
from invoices.models import Invoice, InvoiceItems
from invoices.forms import InvoiceForm, InvoiceItemsForm
from companies.models import Company


InvoiceItemFormSet = inlineformset_factory(Invoice, InvoiceItems, form=InvoiceItemsForm, extra=1)


class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/invoice-form.html'
    success_url = reverse_lazy('invoice-list')

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['formset'] = InvoiceItemFormSet(self.request.POST)
        else:
            ctx['formset'] = InvoiceItemFormSet()
        ctx['title_bar'] = 'Create Invoice'
        return ctx

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/invoice-form.html'
    success_url = reverse_lazy('invoice-list')

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            # Si se están enviando datos en el POST, se pasa el POST al formset
            ctx['formset'] = InvoiceItemFormSet(self.request.POST, instance=self.object)
        else:
            # Si no, se carga el formset con los ítems existentes de la factura
            ctx['formset'] = InvoiceItemFormSet(instance=self.object)
        ctx['title_bar'] = 'Update Invoice'
        return ctx

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            # Guarda la factura primero
            self.object = form.save()
            # Luego guarda los ítems asociados
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoice/invoice-confirm-delete.html'
    success_url = reverse_lazy('invoice-list')

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Invoice'
        return ctx


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice/invoice-list.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        company = Company.get_by_user(self.request.user)
        return Invoice.get_bills(company)

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Sales Invoices List'
        ctx['action_type'] = None
        ctx['module_name'] = 'invoice'
        ctx['url_new'] = reverse_lazy('invoice-create')
        return ctx


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice/invoice-detail.html'
    context_object_name = 'invoice'

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Invoice Detail'
        return ctx
