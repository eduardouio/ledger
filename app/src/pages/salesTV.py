from django.views.generic import TemplateView


# /invoice
class salesTV(TemplateView):
    template_name = 'pages/sales.html'

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx["title_bar"] = "Sales Module"
        return self.render_to_response(ctx)
