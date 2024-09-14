from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from inventary.models import InventoryMovement
from inventary.forms import InventoryMovementForm
from companies.models import Company


class InventoryMovementCreateView(CreateView):
    model = InventoryMovement
    form_class = InventoryMovementForm
    template_name = 'inventorymovement/inventorymovement-form.html'
    success_url = reverse_lazy('inventorymovement-list')

    def get_context_data(self, **kwargs):
        ctx = super(InventoryMovementCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Inventory Movement'
        return ctx


class InventoryMovementUpdateView(UpdateView):
    model = InventoryMovement
    form_class = InventoryMovementForm
    template_name = 'inventorymovement/inventorymovement-form.html'
    success_url = reverse_lazy('inventorymovement-list')

    def get_context_data(self, **kwargs):
        ctx = super(InventoryMovementUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Inventory Movement'
        return ctx


class InventoryMovementDeleteView(DeleteView):
    model = InventoryMovement
    template_name = 'inventorymovement/inventorymovement-confirm-delete.html'
    success_url = reverse_lazy('inventorymovement-list')

    def get_context_data(self, **kwargs):
        ctx = super(InventoryMovementDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Inventory Movement'
        return ctx


class InventoryMovementListView(ListView):
    model = InventoryMovement
    template_name = 'inventorymovement/inventorymovement-list.html'
    context_object_name = 'inventory_movements'

    def get_queryset(self):
                # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return InventoryMovement.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return InventoryMovement.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(InventoryMovementListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Inventory Movements List'
        return ctx


class InventoryMovementDetailView(DetailView):
    model = InventoryMovement
    template_name = 'inventorymovement/inventorymovement-presentation.html'
    context_object_name = 'inventory_movement'

    def get_context_data(self, **kwargs):
        ctx = super(InventoryMovementDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Inventory Movement Detail'
        return ctx
