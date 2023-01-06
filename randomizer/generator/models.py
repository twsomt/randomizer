from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class Raffle(models.Model):

    # Fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField(max_length=500)
    link = models.URLField()
    winner = models.URLField()
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    creator = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'raffles'
    )

    class Meta:
        ordering = ('-time_create',)

    def __str__(self):
        return self.title