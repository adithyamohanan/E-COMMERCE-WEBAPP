# Generated by Django 4.2.4 on 2023-08-19 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 15, 1, 41, 579810, tzinfo=datetime.timezone.utc)),
        ),
    ]
