# Generated by Django 4.2.1 on 2023-08-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='ratingdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]