# Generated by Django 3.0.6 on 2020-07-17 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0010_auto_20200717_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='userdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 12, 9, 7, 752445)),
        ),
    ]