# Generated by Django 4.2 on 2024-10-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv_template", "0010_cvtemplate_extra_info_cvtemplate_hobbies"),
    ]

    operations = [
        migrations.AddField(
            model_name="cvanalysis",
            name="suggested_roles",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
