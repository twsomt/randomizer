from django.db import models

class Raffle(models.Model):

    # Fields
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    link = models.URLField()
    winner = models.URLField()
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    creator = models.CharField(max_length=100)

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        super(Brand, self).save(*args, **kwargs)