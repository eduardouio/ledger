from django.urls import reverse_lazy
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

class WarenhouseCreateView(CreateView):
    model = Warenhouse
    form_class = WarenhouseForm
    template_name = 'warenhouse/warenhouse-form.html'
    success_url = reverse_lazy('warenhouse-list')

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Warenhouse'
        return ctx


class WarenhouseUpdateView(UpdateView):
    model = Warenhouse
    form_class = WarenhouseForm
    template_name = 'warenhouse/warenhouse-form.html'
    success_url = reverse_lazy('warenhouse-list')

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Warenhouse'
        return ctx


class WarenhouseDeleteView(DeleteView):
    model = Warenhouse
    template_name = 'warenhouse/warenhouse-confirm-delete.html'
    success_url = reverse_lazy('warenhouse-list')

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Warenhouse'
        return ctx


class WarenhouseListView(ListView):
    model = Warenhouse
    template_name = 'warenhouse/warenhouse-list.html'
    context_object_name = 'warenhouses'

    def get_queryset(self):
                # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return Warenhouse.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Warenhouse.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Warenhouses List'
        return ctx


class WarenhouseDetailView(DetailView):
    model = Warenhouse
    template_name = 'warenhouse/warenhouse-presentation.html'
    context_object_name = 'warenhouse'

    def get_context_data(self, **kwargs):
        ctx = super(WarenhouseDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Warenhouse Detail'
        return ctx
