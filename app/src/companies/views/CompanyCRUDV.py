from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from companies.models import Company
from companies.forms import CompanyForm


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company-form.html'
    success_url = reverse_lazy('company-list')

    def get_context_data(self, **kwargs):
        ctx = super(CompanyCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Company'
        return ctx


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company-form.html'
    success_url = reverse_lazy('company-list')

    def get_context_data(self, **kwargs):
        ctx = super(CompanyUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Company'
        return ctx


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company/company-confirm-delete.html'
    success_url = reverse_lazy('company-list')

    def get_context_data(self, **kwargs):
        ctx = super(CompanyDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Company'
        return ctx


class CompanyListView(ListView):
    model = Company
    template_name = 'company/company-list.html'
    context_object_name = 'companies'

    def get_queryset(self):
                # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return Company.objects.none()
        if not self.request.user.is_authenticated:
            return Company.objects.none()
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(CompanyListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Company List'
        return ctx


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company-presentation.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        ctx = super(CompanyDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Company Detail'
        return ctx

