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


class PartnerCreateView(CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/partner-form.html'
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, **kwargs):
        ctx = super(PartnerCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Partner'
        return ctx


class PartnerUpdateView(UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/partner-form.html'
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, **kwargs):
        ctx = super(PartnerUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Partner'
        return ctx


class PartnerDeleteView(DeleteView):
    model = Partner
    template_name = 'partner/partner_confirm-delete.html'
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, **kwargs):
        ctx = super(PartnerDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Partner'
        return ctx


class PartnerListView(ListView):
    model = Partner
    template_name = 'partner/partner-list.html'
    context_object_name = 'partners'

    def get_queryset(self):
        # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return Partner.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Partner.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(PartnerListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Partners List'
        return ctx


class PartnerDetailView(DetailView):
    model = Partner
    template_name = 'partner/partner-presentation.html'
    context_object_name = 'partner'

    def get_context_data(self, **kwargs):
        ctx = super(PartnerDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Partner Detail'
        return ctx
