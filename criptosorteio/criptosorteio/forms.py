from django.utils.translation import ugettext as _
from django import forms
from django.contrib.auth.models import User

from django.template import Template
from material import Layout, Row, Column, Fieldset

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=128, required=True, label="Nome", 
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome...'}))

    last_name = forms.CharField(max_length=128, required=True, label="Sobrenome",
        widget=forms.TextInput(attrs={'placeholder': 'Seu sobrenome...'}))

    username = forms.CharField(min_length=4, max_length=150, required=True, label="Usuario",
        widget=forms.TextInput(attrs={'placeholder': 'Seu usuario...'}))

    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha...'}))

    password_confirm = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha...'}))

    email = forms.EmailField(required=True, label="Email")

    agree_toc = forms.BooleanField(required=True, label='Eu concordo com os termos do Criptosorteio')

    layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Detalhes pessoais',
                             Row('first_name', 'last_name'),
                             'agree_toc'))

    title = 'Cadastro de usuario'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(_('Email ja utilizado.'))
        return email

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError(_("As senhas não conferem"))

class UpdateUserForm(forms.Form):
    first_name = forms.CharField(max_length=128, required=True, label="Nome", 
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome...'}))

    last_name = forms.CharField(max_length=128, required=True, label="Sobrenome",
        widget=forms.TextInput(attrs={'placeholder': 'Seu sobrenome...'}))

    email = forms.EmailField(required=True, label="Email")        

    current_password = forms.CharField(required=True, label="Senha Atual",
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha...'}))

    layout = Layout(Row('first_name', 'last_name'), 'email', 'current_password')

class UpdatePasswordForm(forms.Form):
    current_password = forms.CharField(required=True, label="Senha Atual",
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha...'}))

    new_password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua nova senha...'}))

    password_confirm = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha...'}))

    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        new_password = cleaned_data.get("new_password")
        password_confirm = cleaned_data.get("password_confirm")

        if new_password != password_confirm:
            raise forms.ValidationError(_("As senhas não conferem"))