from django import forms

from generator.models import Raffle


class VkForm(forms.ModelForm):
    class Meta:
        # Raffle form
        model = Raffle
        fields = ('title', 'slug', 'description', 'link', 'winner', 'creator')

    def clean(self):
        print(type(self.cleaned_data))
        print(self.cleaned_data)
        self.cleaned_data['title'] = self.cleaned_data['title'].lower()
        self.cleaned_data['description'] = self.cleaned_data['description'].lower()
        # for k, v in self.cleaned_data.items():
        #     print(f'Ключ: {k} // Значение: {v}')