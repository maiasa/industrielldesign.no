# Generated by Django 2.0.1 on 2018-08-03 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0008_auto_20180512_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
    ]