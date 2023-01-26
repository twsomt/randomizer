from django.urls import path
from user_cabinet.views import *

app_name = 'user_cabinet'
urlpatterns = [
    path('', index_lk, name='index_lk'),
]


