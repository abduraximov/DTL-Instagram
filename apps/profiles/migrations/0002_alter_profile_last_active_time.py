# Generated by Django 4.2.4 on 2023-08-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_active_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last active time'),
        ),
    ]
