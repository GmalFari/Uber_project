# Generated by Django 4.2.1 on 2023-07-27 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_number', models.BigIntegerField()),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('alternet_number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_type', models.CharField(blank=True, max_length=50, null=True)),
                ('package', models.CharField(choices=[('4Hours', '4Hours'), ('8Hours', '8Hours'), ('Night', 'Night')], default='4Hours', max_length=20)),
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
            ],
        ),
    ]
