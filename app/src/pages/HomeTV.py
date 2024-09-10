from django.views.generic import TemplateView


# /
class HomeTV(TemplateView):
    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx["title_bar"] = "Home"
        return self.render_to_response(ctx)
