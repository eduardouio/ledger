from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Create Product'
        ctx['company'] = Company.get_by_user(self.request.user)
        return ctx

    def get_success_url(self) -> str:
        url = reverse_lazy('product-detail', kwargs={'pk': self.object.pk})
        url += '?action=created'
        return url


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product-form.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdateView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Update Product'
        return ctx

    def get_success_url(self):
        url = reverse_lazy('product-detail', kwargs={'pk': self.object.id})
        url += '?action=updated'
        return url


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        if product.company != Company.get_by_user(request.user):
            raise Exception('User not allowed to delete this product')

        product.delete()
        return HttpResponseRedirect(self.success_url + '?action=deleted')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        my_company = Company.get_by_user(self.request.user)
        if not my_company:
            raise Exception('Company not found')

        if self.request.GET.get('type') == 'product':
            return Product.objects.filter(company=my_company, type='product')
        elif self.request.GET.get('type') == 'service':
            return Product.objects.filter(company=my_company, type='service')

        return Product.objects.filter(company=my_company)

    def get_context_data(self, **kwargs):
        ctx = super(ProductListView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Products/Services List'
        ctx['module_name'] = 'products'
        ctx['type_a_class'] = 'badge border text-xs bg-cyan-600 uppercase text-white'
        ctx['type_b_class'] = 'badge border text-xs bg-green-600 uppercase text-white'
        ctx['filter'] = 'products'
        ctx['url_new'] = reverse_lazy('product-create')
        ctx['url_filter_1'] = reverse_lazy('product-list') + '?type=product'
        ctx['url_filter_2'] = reverse_lazy('product-list') + '?type=service'

        if self.request.GET.get('action') == 'deleted':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Product deleted successfully'

        return ctx


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/product-presentation.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        ctx = super(ProductDetailView, self).get_context_data(**kwargs)
        ctx['title_bar'] = 'Product Detail'
        ctx['action_type'] = None

        if self.request.GET.get('action') == 'updated':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Product updated successfully'
        if self.request.GET.get('action') == 'created':
            ctx['action_type'] = 'success'
            ctx['message'] = 'Product created successfully'
        if self.request.GET.get('action') == 'alert':
            ctx['action_type'] = 'alert'
            ctx['message'] = 'The Partner will be removed, cannot be undone.'

        return ctx
