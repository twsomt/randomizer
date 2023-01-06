from django.shortcuts import render, redirect
from generator.models import Raffle
from generator.models import User

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
    raffles = (Raffle.objects.filter(slug=slug))

    context = {
        'raffles': raffles
    }

    return render(request, 'generator/raffle_page.html', context)
