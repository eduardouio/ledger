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
from inventary.models import Product
from django.core.serializers import serialize


InvoiceItemFormSet = inlineformset_factory(
    Invoice, InvoiceItems,
    form=InvoiceItemsForm,
    extra=20
)


class BillCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'bills/bills-form.html'
    success_url = reverse_lazy('bills-list')

    def get_context_data(self, **kwargs):
        ctx = super(BillCreateView, self).get_context_data(**kwargs)
        company = Company.get_by_user(self.request.user)
        ctx['company'] = company
        ctx['title_bar'] = 'Create Bill Invoice'
        products =  Product.get_all(company)
        ctx['products'] = serialize('json', products)
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


class BillDeleteView(DeleteView):
    model = Invoice
    template_name = 'bills/bills-confirm-delete.html'
    success_url = reverse_lazy('invoice-list')

    def get_context_data(self, **kwargs):
        ctx = super(BillDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Invoice'
        return ctx


class BillListView(ListView):
    model = Invoice
    template_name = 'bills/bills-list.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        company = Company.get_by_user(self.request.user)
        return Invoice.get_bills(company)

    def get_context_data(self, **kwargs):
        ctx = super(BillListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Sales Invoices List'
        ctx['action_type'] = None
        ctx['module_name'] = 'bills'
        ctx['url_new'] = reverse_lazy('bills-create')
        return ctx


class BillDetailView(DetailView):
    model = Invoice
    template_name = 'bills/bills-detail.html'
    context_object_name = 'invoice'

    def get_context_data(self, **kwargs):
        ctx = super(BillDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Invoice Detail'
        return ctx
