# Generated by Django 4.2.1 on 2023-08-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddriver',
            name='driver_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], default='Temporary', max_length=10),
        ),
    ]