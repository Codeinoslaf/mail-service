# Generated by Django 5.2.1 on 2025-06-05 08:43

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_email_task_alter_task_created_at'),
    ]

    operations = [

        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 5, 8, 43, 23, 774134)),
        ),
    ]
