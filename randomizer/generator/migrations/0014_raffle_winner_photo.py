# Generated by Django 4.1.4 on 2023-01-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0013_raffle_winner_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='raffle',
            name='winner_photo',
            field=models.TextField(default='photo', verbose_name='Ссылка на фото победителя'),
            preserve_default=False,
        ),
    ]
