# Generated by Django 2.2.2 on 2019-11-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo', '0007_auto_20190902_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontaktperson',
            name='rank',
            field=models.PositiveSmallIntegerField(default='0'),
        ),
    ]