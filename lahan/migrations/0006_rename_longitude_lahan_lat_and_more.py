# Generated by Django 4.1.3 on 2023-02-11 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lahan', '0005_remove_lahan_address_remove_lahan_fullname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lahan',
            old_name='longitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='lahan',
            old_name='magnitude',
            new_name='long',
        ),
    ]
