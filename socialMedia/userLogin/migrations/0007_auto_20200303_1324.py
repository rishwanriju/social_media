# Generated by Django 3.0.2 on 2020-03-03 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userLogin', '0006_auto_20200303_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dlogin',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 3, 13, 24, 3, 932173)),
        ),
        migrations.RemoveField(
            model_name='post_like',
            name='p_likes',
        ),
        migrations.AddField(
            model_name='post_like',
            name='p_likes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to='userLogin.dlogin'),
        ),
    ]
