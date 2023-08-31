# Generated by Django 4.2.1 on 2023-08-31 21:21

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placebooking',
            name='drop_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='placebooking',
            name='pickup_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='placebooking',
            name='currant_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, help_text='Point(currentlocation longitude latitude)', null=True, srid=4326),
        ),
    ]
