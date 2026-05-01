import random
import string

from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse

from django.contrib.auth import login
from django.views.generic.base import TemplateView
from django.views import View
from django.http import JsonResponse, HttpRequest
from django.core.mail import send_mail

from django.conf import settings

from .forms import EmailUserCreationForm, EmailAuthenticatedForm, EmailVerificationForm

class AuthTemplateView(TemplateView):
    template_name = 'user_app/auth.html'
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form_register"] = EmailUserCreationForm()
        context['form_login'] = EmailAuthenticatedForm()
        context['form_confirm_email'] = EmailVerificationForm()
        return context

class RegisterView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False

            user.save()

            request.session['confirmation_code'] = ''.join([random.choice(string.digits) for i in range(6)])

            send_mail('Регистрация на сайте', f'Подтвердите регистрацию на сайте\n Дорогой пользователь! На вашу почту регистрируют аккаунт на сайте!!! Вот ваш код: {request.session['confirmation_code']}.\nЕсли вы не знаете что это, игнорируйте это сообщение.', from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[user.email], fail_silently=False)

            return JsonResponse({
                'success': True,
                'message': 'Аккаунт зарегистрирован, для активации подтвердите почту.'
            })

        print(form.errors.get_json_data())
        return JsonResponse({
            'success': False,
            'errors': form.errors.get_json_data()
        }, status= 400)
        
class LoginView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        form = EmailAuthenticatedForm(request= request, data= request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request= request, user= user)
            return redirect('chat')
        # 
        return JsonResponse({
            "success": True,
            'errors': form.errors.get_json_data()
        })

class ActivateAccountView(View):
    def post(self, request: HttpRequest):
        form = EmailVerificationForm(request.POST)
        if not form.is_valid():
            print(form.errors.get_json_data())
            return JsonResponse({
                'success': False,
                'errors': form.errors.get_json_data()
            })

        code_obj = get_object_or_404(ConfirmationCode, id=int(form.cleaned_data.get('code_id')))

        if code_obj.code == str(form.get_full_code()):
            code_obj.target_user.is_active = True
            code_obj.expired = True
            code_obj.delete()

            print('ok')
            return JsonResponse({
                'success': True,
                'next': reverse('auth')
            })
        else:
            print('invalid code')
            return JsonResponse({
                'success': False,
                'errors': 'Invalid code entered!'
            })

