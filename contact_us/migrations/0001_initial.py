# Generated by Django 4.2 on 2024-10-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(blank=True, max_length=20)),
                ("query", models.TextField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
