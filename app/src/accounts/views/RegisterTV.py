from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from accounts.models import CustomUserModel


# /accounts/login/
class LoginTV(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        page_data = {
            'title_page': 'Inicio Sesion',
            'module_name': 'Accounts',
            'message': '',
            'satus': 'not_logged_in',
        }
        if request.user.is_authenticated:
            page_data['status'] = 'logged_in'
            page_data['message'] = 'Ya has iniciado sesion'
            return HttpResponseRedirect('/home-rv/')

        context = self.get_context_data(**kwargs)
        return self.render_to_response({**context, **page_data})
