# Generated by Django 3.0.6 on 2020-07-17 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0024_auto_20200717_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='id',
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='userdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 17, 19, 38, 455019)),
        ),
    ]
