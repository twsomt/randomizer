from django.shortcuts import render
from generator.views import authorized_only

@authorized_only
def index_lk(request):
    return render(request, 'user_cabinet/index_lk.html', {})