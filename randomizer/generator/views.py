from django.shortcuts import render, redirect
from generator.models import Raffle
from django.views.generic.edit import CreateView
from generator.forms import VkForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime as dt

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

class VkForm(LoginRequiredMixin, CreateView): 
    form_class = VkForm
    model = Raffle
    template_name = 'generator/rfl.html'
    success_url = '/thankyou/' 

    def form_valid(self, form):
        
        form.instance.creator = self.request.user
        user = form.instance.creator
        pk = form.instance.pk
        # title
        title = form.instance.title
        now = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        print(now)
        if not title:
            form.instance.title = f'Конкурс #{user}_{now}'

        # description
        description = form.instance.description
        if not description:
            form.instance.description = f'Конкурс #{user}_{now}'

         # winner
        winner = form.instance.winner
        if not winner:
            form.instance.winner = 'https://vk.com/id10883203'
        
        return super().form_valid(form)
