from django.shortcuts import render
from generator.views import authorized_only
from generator.models import Client
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from user_cabinet.forms import DisplayNameUpdate




@authorized_only
def index_lk(request):
    return render(request, 'user_cabinet/index_lk.html', {})

def display_name_update(request):
    return render(request, 'user_cabinet/display_name_update_form.html', {} )

def display_name_update_ok(request):
    display_name = request.POST.get('display_name')
    usr = Client.objects.get(user=request.user)
    usr.display_name = display_name
    usr.save()
    
    if display_name:
        text = 'Псевдоним успешно изменен на'
        name = display_name
    else:
        text = 'Псевдоним успешно сброшен'
        name = ''

    context = {
        'text':text,
        'name':name,
    }
    return render(request, 'user_cabinet/display_name_update_complete.html', context )

class DisplayNameUpdate(LoginRequiredMixin, CreateView):
    form_class = DisplayNameUpdate
    model = Client
    template_name = 'user_cabinet/display_name_update_form.html'
    success_url = '/display_name_update_ok/'