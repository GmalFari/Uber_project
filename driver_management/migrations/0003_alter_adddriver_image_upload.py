# Generated by Django 4.2.1 on 2023-08-16 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_management', '0002_adddriver_driver_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddriver',
            name='image_upload',
            field=models.ImageField(default=None, upload_to='media'),
        ),
    ]
