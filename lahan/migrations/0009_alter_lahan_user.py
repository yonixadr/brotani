# Generated by Django 4.1.3 on 2023-02-12 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lahan', '0008_alter_lahan_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lahan',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lahan', to=settings.AUTH_USER_MODEL),
        ),
    ]