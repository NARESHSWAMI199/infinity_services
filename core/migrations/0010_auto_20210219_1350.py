# Generated by Django 3.1.6 on 2021-02-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_userdetail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='work',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='work',
            field=models.ManyToManyField(to='core.Service'),
        ),
    ]
