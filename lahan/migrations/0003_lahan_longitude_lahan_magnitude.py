# Generated by Django 4.1.3 on 2023-02-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lahan', '0002_lahan_namegreenhouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='lahan',
            name='longitude',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lahan',
            name='magnitude',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
    ]
