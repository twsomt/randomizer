from django.shortcuts import render
from generator.models import Raffle

def index(request):
    raffles = (Raffle.objects.all())

    context = {
        'raffles': raffles
    }

    return render(request, 'generator/index.html', context)
