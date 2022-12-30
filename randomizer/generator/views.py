from django.shortcuts import render
from generator.models import Raffle

def index(request):
    raffles = (Raffle.objects.all())[::-1]

    context = {
        'raffles': raffles
    }

    return render(request, 'generator/index.html', context)


def raffle_page(request, slug):
    raffle = (Raffle.objects.all())

    context = {
        'raffle': raffle
    }

    return render(request, 'generator/raffle_page.html', context)
