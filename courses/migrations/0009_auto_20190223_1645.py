# Generated by Django 2.0.1 on 2019-02-23 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0008_auto_20190223_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('course_code', models.CharField(max_length=20)),
                ('class_year', models.CharField(choices=[('1.klasse', '1.klasse'), ('2.klasse', '2.klasse'), ('3.klasse', '3.klasse'), ('4.klasse', '4.klasse'), ('5.klasse', '5.klasse'), ('Ikke trinnavhengig', 'Ikke trinnavhengig')], default='Ikke trinnavhengig', max_length=20)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_title', models.CharField(max_length=500)),
                ('url_description', models.TextField()),
                ('img_url', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='reviews',
            field=models.ManyToManyField(to='courses.CourseReview'),
        ),
    ]
