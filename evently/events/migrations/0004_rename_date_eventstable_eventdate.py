# Generated by Django 5.0.6 on 2024-05-29 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_eventstable_attendees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventstable',
            old_name='date',
            new_name='eventDate',
        ),
    ]