from typing import Any

from django.shortcuts import render
from django.views.generic import TemplateView

from user_app.forms import LoginForm , ConfirmForm, RegisterForm
# Create your views here.

class UserView(TemplateView):
    template_name = "user_app/user_main.html"

class AuthTemplateView(TemplateView):
    template_name = 'user_app/auth.html'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        \
        context["form_register"] = RegisterForm()
        context['form_login'] = LoginForm()
        context['form_confirm_email'] = ConfirmForm()

        return context