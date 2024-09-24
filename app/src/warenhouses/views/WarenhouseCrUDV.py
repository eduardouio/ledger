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
from warenhouses.models import Warenhouse
from warenhouses.forms import WarenhouseForm
from companies.models import Company


class WarenhouseCreateView(LoginRequiredMixin, CreateView):
    model = Warenhouse
    form_class = WarenhouseForm
    template_name = 'warenhouse/warenhouse-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseCreateView, self).get_context_data(**kwargs)
        company = Company.get_by_user(self.request.user)
        ctx['title_bar'] = 'Create Warenhouse'
        ctx['company'] = company
        return ctx

    def get_success_url(self):
        url = reverse_lazy('warenhouse-detail', kwargs={'pk': self.object.pk})
        url += '?action=created'
        return url


class WarenhouseUpdateView(LoginRequiredMixin, UpdateView):
    model = Warenhouse
    form_class = WarenhouseForm
    template_name = 'warenhouse/warenhouse-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Warenhouse'
        return ctx

    def get_success_url(self):
        url = reverse_lazy('warenhouse-detail', kwargs={'pk': self.object.pk})
        url += '?action=created'
        return url


class WarenhouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Warenhouse
    success_url = reverse_lazy('warenhouse-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.company != Company.get_by_user(request.user):
            raise Exception('Not allowed to delete this warenhouse')

        self.object.delete()
        return HttpResponseRedirect(self.success_url + '?action=deleted')


class WarenhouseListView(LoginRequiredMixin, ListView):
    model = Warenhouse
    template_name = 'warenhouse/warenhouse-list.html'
    context_object_name = 'warenhouses'

    def get_queryset(self):
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Warenhouse.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Warenhouses List'
        ctx['module_name'] = 'warenhouses'
        ctx['url_new'] = reverse_lazy('warenhouse-create')
        ctx['action_type'] = None
        if self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Warenhouse deleted successfully'
        return ctx


class WarenhouseDetailView(LoginRequiredMixin, DetailView):
    model = Warenhouse
    template_name = 'warenhouse/warenhouse-presentation.html'
    context_object_name = 'warenhouse'

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Warenhouse Detail'
        ctx['action_type'] = None
        if self.request.GET.get('action') == 'created':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Warenhouse created successfully'
        if self.request.GET.get('action') == 'updated':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Warenhouse updated successfully'
        if self.request.GET.get('action') == 'alert':
            ctx['action_type'] = 'alert'
            ctx['message'] = 'The Warenhouse will be removed, cannot be undone'
        return ctx
