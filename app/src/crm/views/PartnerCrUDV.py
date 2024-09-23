from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from crm.models import Partner
from crm.forms import PartnerForm
from companies.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


# /crm/partner/add
class PartnerCreateView(LoginRequiredMixin, CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'crm/partner-form.html'
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, *args, **kwargs):
        ctx = super(PartnerCreateView, self).get_context_data(*args, **kwargs)
        ctx['title_bar'] = 'Create Partner'
        ctx['company'] = Company.get_by_user(self.request.user)
        return ctx

    def get_success_url(self):
        url = reverse_lazy('partner-detail', kwargs={'pk': self.object.id})
        url += '?action=created'
        return url


# /crm/partners/<pk>/edit/
class PartnerUpdateView(LoginRequiredMixin, UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'crm/partner-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(PartnerUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Partner'
        return ctx

    def get_success_url(self):
        url = reverse_lazy('partner-detail', kwargs={'pk': self.object.id})
        url += '?action=updated'
        return url


# /crm/partners/<pk>/delete/
class PartnerDeleteView(LoginRequiredMixin, DeleteView):
    model = Partner
    success_url = reverse_lazy('partner-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        partner = self.get_object()
        if partner.company != Company.get_by_user(request.user):
            raise Exception('Error deleting partner')
        partner.delete()

        return HttpResponseRedirect(self.success_url + '?action=deleted')


# /crm/partners/
class PartnerListView(LoginRequiredMixin, ListView):
    model = Partner
    template_name = 'crm/partner-list.html'
    context_object_name = 'partners'

    def get_queryset(self):
        type_partner = self.request.GET.get('type')
        my_company = Company.get_by_user(self.request.user)
        if not my_company:
            raise Exception('Company not found')

        if type_partner == 'customer':
            return Partner.objects.filter(company=my_company, type='customer')
        elif type_partner == 'supplier':
            return Partner.objects.filter(company=my_company, type='supplier')
        else:
            return Partner.objects.filter(company=my_company)

    def get_context_data(self, **kwargs):
        ctx = super(PartnerListView, self).get_context_data(**kwargs)
        ctx['action_type'] = None
        ctx['filter'] = 'partners'
        
        options = {
            'customer': 1,
            'supplier': 2,
            'all': 0
        }
        ctx['title_bar'] = 'Partners List'
        ctx['customer_class'] = 'badge border text-xs bg-cyan-600 uppercase text-white'
        ctx['supplier_class'] = 'badge border text-xs bg-green-600 uppercase text-white'
        ctx['url_filter_1'] = reverse_lazy('partner-list') + '?type=customer'
        ctx['url_filter_2'] = reverse_lazy('partner-list') + '?type=supplier'
        ctx['url_base'] = reverse_lazy('partner-list')
        ctx['option'] = options.get(self.request.GET.get('type', 'all'))
        if self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Partner deleted successfully'
        return ctx


# /crm/partners/<pk>/
class PartnerDetailView(LoginRequiredMixin, DetailView):
    model = Partner
    template_name = 'crm/partner-presentation.html'
    context_object_name = 'partner'

    def get_context_data(self, **kwargs):
        ctx = super(PartnerDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Partner Detail'
        ctx['action_type'] = None
        if self.request.GET.get('action') == 'updated':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Partner updated successfully'
        if self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Partner deleted successfully'
        if self.request.GET.get('action') == 'created':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Partner created successfully'
        if self.request.GET.get('action') == 'alert':
            ctx['action_type'] = 'alert'
            ctx['message'] = 'The Partner will be removed, cannot be undone.'

        return ctx
