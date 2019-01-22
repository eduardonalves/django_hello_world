from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.conf import settings
from . forms import RegisterForm, EditAccountForm, PasswordResetForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import PasswordReset
from core.utils import generate_hash_key

# Create your views here.
#Chama a função login_required antes de entrar na função dashboard
@login_required
def dashboard(request):
	template_name = 'registration/dashboard.html'
	context = {}
	return  render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'registration/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'registration/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

def register(request):
	template_name = 'registration/register.html'

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username=request.POST['username']
			password=request.POST['password1']
			user3=authenticate(request, username=username, password=password)
			if user3 is not None:
				login(request, user3)
				return redirect(settings.LOGIN_REDIRECT_URL)
			else:
				return redirect(settings.LOGIN_URL)

	else:
		form = RegisterForm()

	context = {
		'form': form
	}
	return  render(request, template_name, context)

def password_reset(request):
    template_name = 'registration/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'registration/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_done(request):
	template_name = 'registration/password_reset_done.html'
	context = {}
	form = PasswordResetForm(request.POST or None) #preencher com os dados do post ou None (vazio)
	if form.is_valid():
		form.save()
		context['success'] = True
	
	context['form'] = form	
				
	return render(request, template_name,context)
