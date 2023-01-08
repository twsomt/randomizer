from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from django.core.validators import MinValueValidator

User = get_user_model()


class Raffle(models.Model):

    # Fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField(max_length=500)
    link = models.URLField()
    is_subscribers = models.BooleanField(default=True)
    winner = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='raffles',
    )

    class Meta:
        ordering = ('-time_create',)

    def __str__(self):
        return self.title


class Client(models.Model):

    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    api_vk_key = models.CharField(null=True, max_length=500)
    paid_up_to = models.DateField(null=True)

    def __str__(self):
        return self.user.get_username()
