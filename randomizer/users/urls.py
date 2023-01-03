from django.contrib.auth.views import LogoutView 
from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('signup/', SignUp.as_view(), name='signup')
]