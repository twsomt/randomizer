from django import forms

from generator.models import Raffle


class VkForm(forms.ModelForm):
    class Meta:
        # Raffle form
        model = Raffle
        fields = ('slug', 'link', 'qty_winners', 'is_subscribers')
