# Generated by Django 5.0.3 on 2024-04-27 19:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("quality_control", "0002_remove_bugreport_priority_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bugreport",
            old_name="proirity",
            new_name="priority",
        ),
        migrations.RenameField(
            model_name="featurerequest",
            old_name="proirity",
            new_name="priority",
        ),
    ]
