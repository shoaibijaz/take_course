# Generated by Django 3.0.4 on 2020-03-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_courses', '0002_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='course_images/%Y/%m'),
        ),
    ]
