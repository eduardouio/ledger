from django.views.generic import TemplateView


# /
class HomeTV(TemplateView):
    template_name = 'base/base.html'

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        return self.render_to_response(ctx)