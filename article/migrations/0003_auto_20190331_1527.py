# Generated by Django 2.1.7 on 2019-03-31 07:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190328_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 31, 7, 27, 33, 477013, tzinfo=utc)),
        ),
    ]
