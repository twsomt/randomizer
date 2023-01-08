from django.shortcuts import render, redirect
from generator.models import Raffle
from django.views.generic.edit import CreateView
from generator.forms import VkForm

def authorized_only(func):
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')        
    return check_user


@authorized_only
def index(request):
    raffles = (Raffle.objects.filter(creator=request.user))[:5]
    context = {
        'raffles': raffles
    }

    return render(request, 'generator/index.html', context)


@authorized_only
def raffle_page(request, slug):
    raffles = (Raffle.objects.filter(creator=request.user, slug=slug))

    context = {
        'raffles': raffles
    }

    return render(request, 'generator/raffle_page.html', context)

@authorized_only
def my_raffles(request):
    raffles = (Raffle.objects.filter(creator=request.user))

    context = {
        'raffles': raffles
    }

    return render(request, 'generator/my_raffles.html', context)

@authorized_only
def thankyou(request):
    raffles = (Raffle.objects.filter(creator=request.user))[:1]
    context = {
        'raffles': raffles
    }
    return render(request, 'generator/thx.html', context)

class VkForm(CreateView): 
    form_class = VkForm    
    template_name = 'generator/rfl.html'
    success_url = '/thankyou/' 
