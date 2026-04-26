from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.base import TemplateView
from django.views import View
from django.http import JsonResponse, HttpRequest

from .forms import EmailUserCreationForm, EmailAuthenticatedForm
# Create your views here.
class AuthTemplateView(TemplateView):
    template_name = 'user_app/auth.html'
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form_register"] = EmailUserCreationForm()
        context['form_login'] = EmailAuthenticatedForm()
        context['form_confirm_email'] = ''
        return context
    
    
class RegisterView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Користувача успішно зареєстровано'
            })
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

from django.shortcuts import render, redirect
from django.contrib import messages
from .email import AccountVerificationEmail
from .forms import EmailVerificationForm


def send_verification_email(request, email):
    """Generate code, send email, save to session."""
    email_msg = AccountVerificationEmail(to_email=email)
    code = email_msg.get_code()
    
    # Save code to session (or database in production)
    request.session['verification_code'] = code
    request.session['verification_email'] = email
    
    email_msg.send()
    return code


def confirm_email(request):
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            entered_code = form.get_full_code()
            saved_code = request.session.get('verification_code')
            
            if entered_code == saved_code:
                messages.success(request, 'Email confirmed!')
                # Clear code from session
                del request.session['verification_code']
                return redirect('success_page')
            else:
                messages.error(request, 'Incorrect code. Try again.')
    else:
        form = EmailVerificationForm()
    
    return render(request, 'confirm_email.html', {
        'form_confirm_email': form,
    })
        
        