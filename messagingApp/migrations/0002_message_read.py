# Generated by Django 3.0.7 on 2020-06-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
