# Generated by Django 3.0.6 on 2020-07-11 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='userdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 11, 16, 9, 19, 181031)),
        ),
    ]
