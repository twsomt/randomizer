# Generated by Django 4.1.4 on 2023-01-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0016_alter_raffle_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffle',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Какой будет приз?'),
        ),
    ]