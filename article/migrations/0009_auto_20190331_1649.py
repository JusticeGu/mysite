# Generated by Django 2.1.7 on 2019-03-31 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20190331_1638'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='articlepost',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='articlepost',
            name='autror',
        ),
        migrations.RemoveField(
            model_name='articlepost',
            name='column',
        ),
        migrations.DeleteModel(
            name='ArticlePost',
        ),
    ]
