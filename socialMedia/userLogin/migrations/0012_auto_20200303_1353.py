# Generated by Django 3.0.2 on 2020-03-03 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userLogin', '0011_auto_20200303_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dlogin',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 3, 13, 53, 26, 921080)),
        ),
    ]