from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator

class LoginRequired(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequired, self).dispatch(*args, **kwargs)
