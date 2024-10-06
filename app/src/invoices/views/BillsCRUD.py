import json
from datetime import datetime
from decimal import Decimal
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import (
    TemplateView,
    DeleteView,
    ListView,
    DetailView
)
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from invoices.models import Invoice, InvoiceItems
from crm.models import Partner
from companies.models import Company
from inventary.models import Product


class BillCreateView(LoginRequiredMixin, TemplateView):
    model = Invoice
    template_name = 'bills/bill-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(BillCreateView, self).get_context_data(**kwargs)
        company = Company.get_by_user(self.request.user)
        ctx['company'] = company
        products = Product.get_all(ctx['company'])
        partners = Partner.get_suppliers(ctx['company'])
        ctx['title_bar'] = 'Create Bill Invoice'
        ctx['products'] = serialize('json', products)
        ctx['suppliers'] = serialize('json', partners)
        ctx['company_data'] = serialize('json', [company])
        return ctx

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        invoice_data = data['invoice_headers']
        line_items = data['invoice_items']
        company = Company.get_by_user(request.user)
        supplier = Partner.get_by_id(invoice_data['supplier']['id'])
        invoice = Invoice.objects.create(
            company=company,
            partner=supplier,
            type='BILL',
            date=datetime.fromisoformat(invoice_data['date']),
            due_date=datetime.fromisoformat(invoice_data['due_date']),
            number=invoice_data['number'],
            amount=Decimal(invoice_data['total']),
            tax=Decimal(invoice_data['tax']),
            discount=Decimal(invoice_data['discount']),
            pay_terms=invoice_data['pay_terms'],
            status='ACEPTED',
            user=request.user
        )

        for item in line_items:
            product = Product.get_by_id(item['product']['id'], company)
            InvoiceItems.objects.create(
                invoice=invoice,
                product=product,
                quantity=item['quantity'],
                price=item['price'],
                discount=item['discount']
            )
            url = reverse_lazy('bill-detail', kwargs={'pk': invoice.id})
            return JsonResponse({'url': url, 'status': 'ok'}, satatus=201)


class BillListView(ListView):
    model = Invoice
    template_name = 'bills/bill-list.html'
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
        invoice_items = []
        subtotal_1 = 0
        total_discount = 0
        total = 0

        for item in InvoiceItems.get_by_invoice(self.object):
            total += (item.price * item.quantity) - item.discount
            subtotal_1 += item.price * item.quantity
            total_discount += item.discount
            invoice_items.append({
                'product': item.product,
                'quantity': item.quantity,
                'price': item.price,
                'discount': item.discount,
                'total': (item.price * item.quantity) - item.discount
            })
        ctx['invoice_items'] = invoice_items
        ctx['title_bar'] = 'Invoice Detail'
        ctx['total'] = {
            'subtotal': subtotal_1,
            'discount': total_discount,
            'total': total
        }
        ctx['url_new'] = reverse_lazy('bills-create')
        return ctx
