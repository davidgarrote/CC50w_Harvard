# Generated by Django 3.0.8 on 2020-09-23 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20200923_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 18, 40, 59, 876748)),
        ),
    ]
