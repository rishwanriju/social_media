# Generated by Django 3.0.2 on 2020-03-03 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userLogin', '0010_auto_20200303_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dlogin',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 3, 13, 49, 42, 96461)),
        ),
    ]