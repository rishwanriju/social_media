# Generated by Django 3.0.2 on 2020-03-11 07:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userLogin', '0021_auto_20200311_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dlogin',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 11, 12, 56, 27, 234877)),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to='userLogin.dlogin'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='posts',
            field=models.TextField(null=True),
        ),
    ]
