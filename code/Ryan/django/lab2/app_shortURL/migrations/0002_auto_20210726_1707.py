# Generated by Django 3.2.5 on 2021-07-27 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_shortURL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='original_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='links',
            name='short_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
