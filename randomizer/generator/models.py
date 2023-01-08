from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from django.core.validators import MinValueValidator

User = get_user_model()


class Raffle(models.Model):

    # Fields
    title = models.CharField(max_length=200, verbose_name='')
    slug = models.SlugField(unique=True, null=False, verbose_name='')
    description = models.TextField(max_length=500, verbose_name='')
    link = models.URLField(verbose_name='')
    is_subscribers = models.BooleanField(default=True, verbose_name='')
    qty_winners = models.PositiveIntegerField(verbose_name='')
    winner = models.TextField(verbose_name='')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='')
    time_update = models.DateTimeField(auto_now=True, verbose_name='')
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='')
    api_vk_key = models.CharField(null=True, max_length=500, verbose_name='')
    paid_up_to = models.DateField(null=True, verbose_name='')

    def __str__(self):
        return self.user.get_username()
