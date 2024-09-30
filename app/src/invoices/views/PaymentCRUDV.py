from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PaymentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/payment-form.html'
    success_url = reverse_lazy('payment-list')

    def get_context_data(self, **kwargs):
        ctx = super(PaymentCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Payment'
        ctx['company'] = Company.get_by_user(self.request.user)
        return ctx

    def get_success_url(self):
        url = reverse_lazy('payment-detail', kwargs={'pk': self.object.id})
        url += '?action=created'
        return url


class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/payment-form.html'
    success_url = reverse_lazy('payment-list')

    def get_context_data(self, **kwargs):
        ctx = super(PaymentUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Payment'
        return ctx

    def get_success_url(self):
        url = reverse_lazy('payment-detail', kwargs={'pk': self.object.id})
        url += '?action=updated'
        return url


class PaymentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'payment/payment-confirm-delete.html'
    success_url = reverse_lazy('payment-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        payment = Payment.objects.get(pk=kwargs['pk'])
        if payment.company != Company.get_by_user(request.user):
            raise Exception('Payment does not belong to the user')

        payment.delete()
        return HttpResponseRedirect(self.success_url + '?action=deleted')


class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'payment/payment-list.html'
    context_object_name = 'payments'

    def get_queryset(self):
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Payment.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(PaymentListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Payments List'
        ctx['url_new'] = reverse_lazy('payment-create')
        ctx['module_name'] = 'payments'

        if self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'deleted'
            ctx['message'] = 'Payment deleted successfully'

        return ctx


class PaymentDetailView(LoginRequiredMixin, DetailView):
    model = Payment
    template_name = 'payment/payment-presentation.html'
    context_object_name = 'payment'

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Payment Detail'
        ctx['action_type'] = None
        ctx['url_new'] = reverse_lazy('payment-create')

        if self.request.GET.get('action') == 'updated':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Payment updated successfully'
        if self.request.GET.get('action') == 'created':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Payment created successfully'
        if self.request.GET.get('action') == 'alert':
            ctx['action_type'] = 'alert'
            ctx['message'] = 'The Partner will be removed, cannot be undone.'

        return ctx
