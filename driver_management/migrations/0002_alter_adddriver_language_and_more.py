# Generated by Django 4.2.1 on 2023-08-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddriver',
            name='language',
            field=models.CharField(choices=[('Hindi', 'Hindi'), ('English', 'English'), ('Bhojpuri', 'Bhojpuri')], default='Hindi', max_length=100),
        ),
        migrations.AlterField(
            model_name='adddriver',
            name='transmission_type',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Luxury', 'Luxury'), ('Both', 'Both')], max_length=10),
        ),
    ]
