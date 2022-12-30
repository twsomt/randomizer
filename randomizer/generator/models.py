from django.db import models
from django.contrib.auth import get_user_model

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

    def __str__(self):
        return self.title