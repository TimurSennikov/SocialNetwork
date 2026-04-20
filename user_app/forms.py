from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class ConfirmForm(forms.Form):
    code = forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=6)

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    

    def clean(self):
        cd = self.cleaned_data()

        p1 = cd.get("password")
        p2 = cd.get("confirm_password")
        if p1 != p2 :
            raise ValidationError("Passwords are not equal")

        return cd
        