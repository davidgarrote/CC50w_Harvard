# Generated by Django 3.0.8 on 2020-09-21 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20200921_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='isreply',
        ),
    ]
