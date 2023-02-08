from django.urls import path
from user_cabinet.views import *

app_name = 'user_cabinet'
urlpatterns = [
    path('', index_lk, name='index_lk'),
    path('display_name_update/', DisplayNameUpdate.as_view(), name='display_name_update'),
    path('display_name_update_ok', display_name_update_ok, name='display_name_update_ok'),
    path('api_key_update', api_key_update, name='api_key_update'),
    path('api_key_update_ok', api_key_update_ok, name='api_key_update_ok'),
]


