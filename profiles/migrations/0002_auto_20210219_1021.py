# Generated by Django 3.1.6 on 2021-02-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/unnamed.png', upload_to='media'),
        ),
    ]