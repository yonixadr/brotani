# Generated by Django 4.1.3 on 2023-03-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadImage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='MultipleImage',
        ),
    ]
