from django.urls import path
from generator.views import *


urlpatterns = [
    path('', index),
]