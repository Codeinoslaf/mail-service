# Generated by Django 5.2.1 on 2025-06-05 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_subject_email_task_task_recipient_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='status',
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 5, 8, 26, 33, 136448)),
        ),
    ]
