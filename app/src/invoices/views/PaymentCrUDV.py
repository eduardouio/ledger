from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from invoices.models import Payment
from invoices.forms import PaymentForm
from companies.models import Company


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/payment-form.html'
    success_url = reverse_lazy('payment-list')

    def get_context_data(self, **kwargs):
        ctx = super(PaymentCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Payment'
        return ctx


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/payment-form.html'
    success_url = reverse_lazy('payment-list')

    def get_context_data(self, **kwargs):
        ctx = super(PaymentUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Payment'
        return ctx


class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment/payment-confirm-delete.html'
    success_url = reverse_lazy('payment-list')

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Payment'
        return ctx


class PaymentListView(ListView):
    model = Payment
    template_name = 'payment/payment-list.html'
    context_object_name = 'payments'

    def get_queryset(self):
                # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return Payment.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Payment.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(PaymentListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Payments List'
        return ctx


class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment/payment-presentation.html'
    context_object_name = 'payment'

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Payment Detail'
        return ctx
