import json
from datetime import date
from decimal import Decimal
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import (
    TemplateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from invoices.models import Invoice, InvoiceItems
from invoices.forms import InvoiceForm, InvoiceItemsForm
from crm.models import Partner
from companies.models import Company
from inventary.models import Product


class InvoiceCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'invoice/invoice-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceCreateView, self).get_context_data(**kwargs)
        company = Company.get_by_user(self.request.user)
        ctx['company'] = company
        products = Product.get_all(ctx['company'])
        partners = Partner.get_customers(ctx['company'])
        ctx['title_bar'] = 'Create Invoice'
        ctx['products'] = serialize('json', products)
        ctx['customers'] = serialize('json', partners)
        ctx['company_data'] = serialize('json', [company])
        ctx['invoice_number'] = Invoice.get_next_invoice_number(ctx['company'])
        ctx['saveURL'] = reverse_lazy('sales-create')
        return ctx

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        invoice_data = data['invoice_headers']
        line_items = data['invoice_items']
        company = Company.get_by_user(request.user)
        customer = Partner.get_by_id(invoice_data['customer']['id'])
        invoice = Invoice.objects.create(
            company=company,
            partner=customer,
            type='Invoice',
            date=date.fromisoformat(invoice_data['date']),
            due_date=date.fromisoformat(invoice_data['due_date']),
            number=invoice_data['number'],
            amount=Decimal(invoice_data['total']),
            tax=Decimal(invoice_data['tax']),
            discount=Decimal(invoice_data['discount']),
            pay_terms=invoice_data['pay_terms'],
            status='acepted',
            user=request.user
        )
        for item in line_items:
            product = Product.get_by_id(item['product']['id'], company)
            InvoiceItems.objects.create(
                invoice=invoice,
                product=product,
                quantity=item['quantity'],
                price=Decimal(item['price']),
                discount=Decimal(item['discount'])
            )
        url = reverse_lazy('sales-detail', kwargs={'pk': invoice.id})
        return JsonResponse({'url': url, 'status': 'ok'}, status=201)


class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    template_name = 'invoice/invoice-confirm-delete.html'
    success_url = reverse_lazy('invoice-list')

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Invoice'
        return ctx


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    template_name = 'invoice/invoice-list.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        company = Company.get_by_user(self.request.user)
        return Invoice.get_invoices(company)

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Sales Invoices List'
        ctx['action_type'] = None
        ctx['module_name'] = 'invoice'
        ctx['url_new'] = reverse_lazy('sales-create')
        return ctx


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'invoice/invoice-detail.html'
    context_object_name = 'invoice'

    def get_context_data(self, **kwargs):
        ctx = super(InvoiceDetailView, self).get_context_data(**kwargs)
        ctx['invoice_items'] = InvoiceItems.get_by_invoice(self.object)
        ctx['title_bar'] = 'Invoice Detail'
        return ctx
