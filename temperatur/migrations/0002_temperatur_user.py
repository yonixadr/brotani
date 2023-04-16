# Generated by Django 4.1.3 on 2023-03-06 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('temperatur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperatur',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='temperatur', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]