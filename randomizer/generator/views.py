from django.shortcuts import render
from generator.models import Raffle

def index(request):
    raffles = (Raffle.objects.all())[:2]

    context = {
        'raffles': raffles
    }

    return render(request, 'generator/index.html', context)


def raffle_page(request, slug):
    raffles = (Raffle.objects.filter(slug=slug))

    context = {
        'raffles': raffles
    }

    return render(request, 'generator/raffle_page.html', context)
