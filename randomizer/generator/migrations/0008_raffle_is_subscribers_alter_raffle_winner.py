# Generated by Django 4.1.4 on 2023-01-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0007_alter_raffle_time_create_alter_raffle_time_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='raffle',
            name='is_subscribers',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='raffle',
            name='winner',
            field=models.TextField(),
        ),
    ]
