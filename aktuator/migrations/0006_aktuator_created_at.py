# Generated by Django 4.1.3 on 2023-03-31 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aktuator', '0005_remove_aktuator_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktuator',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 31, 4, 51, 24, 716545, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]