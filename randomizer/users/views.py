from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.shortcuts import render, redirect

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