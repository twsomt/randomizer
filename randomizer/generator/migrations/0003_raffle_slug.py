# Generated by Django 4.1.4 on 2022-12-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_alter_raffle_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='raffle',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
