# Generated by Django 2.2.2 on 2019-07-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20190728_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
