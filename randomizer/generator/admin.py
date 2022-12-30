from django.contrib import admin
from generator.models import *


@admin.register(Raffle)
class RaffleAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'description',
                    'link',
                    'winner',
                    'time_create',
                    'time_update',
                    'creator',)
            
    prepopulated_fields = {'slug': ('title', )}
