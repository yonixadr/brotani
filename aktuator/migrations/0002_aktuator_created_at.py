# Generated by Django 4.1.3 on 2023-03-31 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aktuator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktuator',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
