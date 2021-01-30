# Generated by Django 3.0.8 on 2020-09-23 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20200923_0952'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follow',
            new_name='Profile',
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(default=None, max_length=140),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 17, 16, 41, 321862)),
        ),
    ]
