from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.shortcuts import render, redirect
from generator.models import Client
from datetime import datetime as dt

def secret_enter(func):
    def check_user(request, *args, **kwargs):
        password = self.request.GET.get('pswrd', '')
        if password == 'lkjr6tyyr416vvv35445dtyb':
            return func(request, *args, **kwargs)
        return redirect('access_denied/')
    return check_user

# @secret_enter
class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('generator:index')
    template_name = 'users/signup.html'
    

def access_denied(request):
    return render(request, 'users/access_denied.html')


def auth_vk_complete(request):
    error = request.GET.get('error', '')
    error_description = request.GET.get('error_description', '')
    context = {
        'error': error,
        'error_description': error_description,
    }
    
    access_token = request.GET.get('token', '123')

    try:
        Client.objects.create(user=request.user, api_vk_key=access_token)
    except:
        Client.objects.update(user=request.user, api_vk_key=access_token)
            

    return render(request, 'users/auth_vk_complete.html', context)



def auth_vk_key(request):
    return render(request, 'users/auth_vk_key.html')