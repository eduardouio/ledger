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


# /crm/partner/add
class PartnerCreateView(LoginRequiredMixin, CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'crm/partner-form.html'
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, *args, **kwargs):
        ctx = self.get_context_data(*args, **kwargs)
        ctx['title_bar'] = 'Create Partner'
        return ctx


# /crm/partners/<pk>/edit/
class PartnerUpdateView(LoginRequiredMixin, UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'crm/partner-form.html'
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, **kwargs):
        ctx = super(PartnerUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Partner'
        return ctx


# /crm/partners/<pk>/delete/
class PartnerDeleteView(LoginRequiredMixin, DeleteView):
    model = Partner
    template_name = 'crm/partner_confirm-delete.html'
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, **kwargs):
        ctx = super(PartnerDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Partner'
        return ctx


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
        return ctx


# /crm/partners/<pk>/
class PartnerDetailView(LoginRequiredMixin, DetailView):
    model = Partner
    template_name = 'crm/partner-presentation.html'
    context_object_name = 'partner'

    def get_context_data(self, **kwargs):
        ctx = super(PartnerDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Partner Detail'
        return ctx
