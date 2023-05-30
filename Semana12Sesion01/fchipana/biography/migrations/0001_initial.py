# Generated by Django 4.2.1 on 2023-05-24 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pais', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Biografia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(max_length=200)),
                ('educado_en', models.TextField()),
                ('ocupacion', models.TextField()),
                ('empleador', models.TextField()),
                ('sitio_web', models.CharField(max_length=200)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biography.nacionalidad')),
                ('nombre_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]