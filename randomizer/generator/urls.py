from django.urls import path
from generator.views import *

app_name = 'generator'
urlpatterns = [
    path('', index, name='index'),
    path('raffles/<slug:slug>/', raffle_page, name='raffle_page')
]


