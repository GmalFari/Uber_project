# Generated by Django 4.2.1 on 2023-07-21 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver_management', '0001_initial'),
        ('booking', '0002_delete_placebooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_type', models.CharField(blank=True, max_length=50, null=True)),
                ('packege', models.CharField(choices=[('4Hours', '4Hours'), ('8Hours', '8Hours'), ('Night', 'Night')])),
                ('user_curr_lat', models.FloatField()),
                ('user_curr_long', models.FloatField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('car_type', models.CharField(max_length=100, null=True)),
                ('gear_type', models.CharField(max_length=100, null=True)),
                ('pickup_location', models.CharField(max_length=100, null=True)),
                ('drop_location', models.CharField(max_length=100, null=True)),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.clientregistration')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_management.adddriver')),
            ],
        ),
    ]