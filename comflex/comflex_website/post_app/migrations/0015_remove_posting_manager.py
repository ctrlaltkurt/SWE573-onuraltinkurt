# Generated by Django 5.0.4 on 2024-04-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0014_posting_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='manager',
        ),
    ]