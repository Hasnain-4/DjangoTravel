# Generated by Django 3.0.6 on 2020-07-17 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0023_auto_20200717_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Starting', models.CharField(max_length=255)),
                ('Ending', models.CharField(max_length=255)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='userdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 17, 16, 17, 54499)),
        ),
    ]