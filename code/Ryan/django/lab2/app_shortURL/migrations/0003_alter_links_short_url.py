# Generated by Django 3.2.5 on 2021-07-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shortURL', '0002_auto_20210726_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='short_url',
            field=models.CharField(max_length=15),
        ),
    ]
