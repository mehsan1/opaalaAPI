# Generated by Django 4.2.18 on 2025-01-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_delete_booklist"),
    ]

    operations = [
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="", max_length=70)),
            ],
        )
    ]
