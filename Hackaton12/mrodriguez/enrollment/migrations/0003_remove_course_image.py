# Generated by Django 4.2.1 on 2023-05-28 00:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("enrollment", "0002_course_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="image",
        ),
    ]