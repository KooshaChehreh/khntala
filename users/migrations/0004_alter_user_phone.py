# Generated by Django 5.1.5 on 2025-01-27 14:07

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[utils.phone_validator], verbose_name='تلفن همراه'),
        ),
    ]
