from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()


class Raffle(models.Model):

    # Fields
    title = models.CharField(max_length=200, verbose_name='Введите заголовок:')
    slug = models.SlugField(unique=True, null=False, verbose_name='Введите слаг-адрес:')
    description = models.CharField(max_length=500, verbose_name='Какой будет приз?')
    link = models.URLField(verbose_name='Введите ссылку на пост Вконтакте:')
    is_subscribers = models.BooleanField(default=True, verbose_name='Учитывать только участников группы')
    qty_winners = models.PositiveIntegerField(verbose_name='Введите желаемое количество победителей:')
    winner = models.TextField(verbose_name='Победитель')
    winner_url = models.TextField(verbose_name='Ссылка на страницу победителя')
    winner_photo = models.TextField(verbose_name='Ссылка на фото победителя')
    winner_first_name = models.TextField(verbose_name='Имя победителя')
    winner_last_name = models.TextField(verbose_name='Фамилия победителя')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания конкурса')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения конкурса')
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='raffles',
        verbose_name=''
    )

    class Meta:
        ordering = ('-time_create',)

    def __str__(self):
        return self.title


class Client(models.Model):

    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='Пользователь')
    api_vk_key = models.CharField(null=True, max_length=500, verbose_name='Ключ VK API')
    paid_up_to = models.DateField(null=True, verbose_name='Оплачено до')

    def __str__(self):
        return self.user.get_username()
