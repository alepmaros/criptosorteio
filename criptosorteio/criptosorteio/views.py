from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

from .forms import RegisterForm, UpdateUserForm, UpdatePasswordForm

class IndexView(TemplateView):
    template_name = "index.html"

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name

            new_user.save()

            return HttpResponseRedirect(reverse('login'))

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def preferencias_view(request):

    form_general_pref = UpdateUserForm(initial={'first_name': request.user.first_name,
                                                'last_name' : request.user.last_name,
                                                'email'     : request.user.email})
    form_change_pw = UpdatePasswordForm()

    err_update = err_change_pw = None

    if request.method == 'POST':
        if '_submit_update_user' in request.POST:
            form_general_pref = UpdateUserForm(request.POST)

            if form_general_pref.is_valid():
                first_name = form_general_pref.cleaned_data['first_name']
                last_name = form_general_pref.cleaned_data['last_name']
                email = form_general_pref.cleaned_data['email']
                current_password = form_general_pref.cleaned_data['current_password']

                # If the email is not being altered or if the email does not belong to another user
                if (not User.objects.filter(email=email).exclude(username=request.user.username).exists()):
                    user = User.objects.get(username=request.user.username)
                    if (user.check_password(current_password)):
                        user.first_name = first_name
                        user.last_name = last_name
                        user.email = email
                        user.save()
                        messages.add_message(request, messages.SUCCESS, 
                            'Cadastro atualizado.', extra_tags='user_update')
                        return HttpResponseRedirect('')
                    else:
                        messages.add_message(request, messages.ERROR,
                            'Senha incorreta', extra_tags='user_update')
                else:
                    messages.add_message(request, messages.ERROR,
                        'E-mail ja utilizado', extra_tags='user_update')

        elif '_submit_change_pw' in request.POST:
            form_change_pw = UpdatePasswordForm(request.POST)

            if form_change_pw.is_valid():
                current_password = form_change_pw.cleaned_data['current_password']
                new_password = form_change_pw.cleaned_data['new_password']

                user = User.objects.get(username=request.user.username)
                if (user.check_password(current_password)):
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.add_message(request, messages.SUCCESS, 
                            'Senha atualizada.', extra_tags='change_pw')
                    return HttpResponseRedirect('')
                else:
                    messages.add_message(request, messages.ERROR,
                        'Senha atual incorreta', extra_tags='change_pw')

    return render(request, 'registration/preferences.html', {'form_general_pref': form_general_pref,
                                                             'form_change_pw'   : form_change_pw})