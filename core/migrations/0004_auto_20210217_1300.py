# Generated by Django 3.1.6 on 2021-02-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_service_short_dis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
