# Generated by Django 4.2.1 on 2023-07-25 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver_management', '0004_alter_adddriver_blood_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driverlocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_lat', models.DecimalField(decimal_places=10, max_digits=10)),
                ('driver_long', models.DecimalField(decimal_places=10, max_digits=10)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]