# Generated by Django 2.2.15 on 2021-05-25 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210525_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]
