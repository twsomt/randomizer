from django import forms

from generator.models import Client


class DisplayNameUpdate(forms.ModelForm):
    class Meta:
        # Client form
        model = Client
        fields = ('display_name',)
