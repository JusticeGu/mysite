# Generated by Django 2.1.7 on 2019-03-31 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190331_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='author',
            new_name='autror',
        ),
    ]
