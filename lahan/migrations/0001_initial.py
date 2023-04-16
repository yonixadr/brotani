# Generated by Django 4.1.3 on 2023-01-25 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='lahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(blank=True, max_length=255)),
                ('fullname', models.CharField(blank=True, max_length=255)),
                ('telephone', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('nib', models.CharField(blank=True, max_length=255)),
                ('addressGreenhouse', models.CharField(blank=True, max_length=255)),
                ('luas', models.CharField(blank=True, max_length=255)),
                ('komoditas', models.CharField(blank=True, max_length=255)),
                ('mitra', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lahan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]