from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
from captcha.fields import CaptchaField


class CreationForm(UserCreationForm):
    captcha = CaptchaField(label='Введите символы с картинки:')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'email')
