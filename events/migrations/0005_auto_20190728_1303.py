# Generated by Django 2.2.2 on 2019-07-28 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_short_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_start_time', 'title'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]
