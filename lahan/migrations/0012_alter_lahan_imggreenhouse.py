# Generated by Django 4.1.3 on 2023-02-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lahan', '0011_lahan_jml_bibit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lahan',
            name='imgGreenhouse',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]