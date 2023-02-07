from django.urls import path
from user_cabinet.views import *

app_name = 'user_cabinet'
urlpatterns = [
    path('', index_lk, name='index_lk'),
    path('display_name_update/', DisplayNameUpdate.as_view(), name='display_name_update'),
    path('display_name_update', display_name_update_ok, name='display_name_update_ok'),
]


