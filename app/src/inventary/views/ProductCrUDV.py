from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)
from inventary.models import Product
from inventary.forms import ProductForm
from companies.models import Company


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product-form.html'
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Product'
        return ctx


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product-form.html'
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Product'
        return ctx


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product-confirm-delete.html'
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        ctx = super(ProductDeleteView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Delete Product'
        return ctx


class ProductListView(ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'products'

    def get_queryset(self):
                # Asegúra usuario esté autenticado
        if not self.request.user.is_authenticated:
            return Product.objects.none()
        my_company = Company.get_by_user(self.request.user)
        if my_company:
            return Product.objects.filter(company=my_company)
        return []

    def get_context_data(self, **kwargs):
        ctx = super(ProductListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Products List'
        return ctx


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-presentation.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        ctx = super(ProductDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Product Detail'
        return ctx
