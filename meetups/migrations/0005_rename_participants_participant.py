# Generated by Django 3.2.7 on 2021-10-02 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20211002_1613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participants',
            new_name='Participant',
        ),
    ]
