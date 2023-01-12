from django.urls import path
from generator.views import *

app_name = 'generator'
urlpatterns = [
    path('', index, name='index'),
    path('raffles/<slug:slug>/', raffle_page, name='raffle_page'),
    path('my_raffles/', my_raffles, name='my_raffles'),
    path('new_raffle/', VkForm.as_view(), name='new_raffle'),
    # path('repeat_rfl/', repeat_rfl, name='repeat_rfl'),
    path('thankyou/', thankyou, name='thankyou'),

]


