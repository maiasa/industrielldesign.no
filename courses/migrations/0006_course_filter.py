# Generated by Django 2.2.1 on 2019-05-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_course_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.CourseFilter'),
        ),
    ]
