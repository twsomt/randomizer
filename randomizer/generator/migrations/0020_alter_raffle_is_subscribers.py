# Generated by Django 4.1.4 on 2023-02-07 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0019_client_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffle',
            name='is_subscribers',
            field=models.BooleanField(default=True, verbose_name='Учитывать только участников группы'),
        ),
    ]
