# Generated by Django 3.1.6 on 2021-02-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_userdetail_timestmap'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='work',
            field=models.CharField(default='not selected', max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]