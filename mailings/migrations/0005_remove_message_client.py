# Generated by Django 5.0 on 2023-12-06 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0004_alter_message_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='client',
        ),
    ]