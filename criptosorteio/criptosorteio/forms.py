from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=128, required=True, label="Nome", 
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome...'}))
    last_name = forms.CharField(max_length=128, required=True, label="Sobrenome",
        widget=forms.TextInput(attrs={'placeholder': 'Seu sobrenome...'}))
    username = forms.CharField(min_length=4, max_length=150, required=True, label="Usuario",
        widget=forms.TextInput(attrs={'placeholder': 'Seu usuario...'}))
    password = forms.CharField(help_text="Senha",
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha...'}))
    email = forms.EmailField(required=True, help_text="Email",
        widget=forms.TextInput(attrs={'placeholder': 'Seu email...'}))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email ja utilizado.')
        return email