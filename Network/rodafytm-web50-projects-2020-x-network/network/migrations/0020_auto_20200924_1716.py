# Generated by Django 3.0.8 on 2020-09-24 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_auto_20200923_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 17, 16, 31, 202563)),
        ),
    ]
