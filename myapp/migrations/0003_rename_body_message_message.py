# Generated by Django 5.1.1 on 2024-09-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_message_message_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='message',
        ),
    ]
