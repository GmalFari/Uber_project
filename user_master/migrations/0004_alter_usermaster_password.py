# Generated by Django 4.2.1 on 2023-07-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_master', '0003_usermaster_password_alter_usermaster_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='password',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
