# Generated by Django 4.2.18 on 2025-01-30 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="list",
        ),
        migrations.DeleteModel(
            name="BookList",
        ),
    ]
