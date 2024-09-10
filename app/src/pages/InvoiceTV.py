from django.views.generic import TemplateView


# /invoice
class InvoiceTV(TemplateView):
    template_name = 'pages/invoice.html'

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx["title_bar"] = "Invoice"
        return self.render_to_response(ctx)