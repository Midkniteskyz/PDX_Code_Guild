# Generated by Django 3.2.6 on 2021-08-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nfl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='draw',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='loss',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='win',
            field=models.IntegerField(default=0),
        ),
    ]
