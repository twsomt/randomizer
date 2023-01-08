from django import forms

from generator.models import Raffle


class VkForm(forms.ModelForm):
    class Meta:
        # Raffle form
        model = Raffle
        fields = ('title', 'slug', 'description', 'link', 'winner')