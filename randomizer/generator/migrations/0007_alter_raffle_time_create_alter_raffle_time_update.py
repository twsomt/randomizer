# Generated by Django 4.1.4 on 2023-01-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffle',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='raffle',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]