# Generated by Django 4.1.4 on 2022-12-09 15:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_appuser_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="phone_number",
            field=models.CharField(
                max_length=10, validators=[django.core.validators.MinLengthValidator(4)]
            ),
        ),
    ]
