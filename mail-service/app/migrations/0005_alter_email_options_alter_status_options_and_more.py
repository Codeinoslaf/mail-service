# Generated by Django 5.2.1 on 2025-06-05 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_email_options_alter_status_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
    ]
