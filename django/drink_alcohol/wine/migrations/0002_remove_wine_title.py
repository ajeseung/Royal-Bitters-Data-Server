# Generated by Django 5.1.4 on 2025-01-12 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wine", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wine",
            name="title",
        ),
    ]