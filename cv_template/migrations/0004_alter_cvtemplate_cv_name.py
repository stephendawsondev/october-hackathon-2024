# Generated by Django 4.2 on 2024-10-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "cv_template",
            "0003_cvtemplate_contact_information_cvtemplate_education_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="cvtemplate",
            name="cv_name",
            field=models.CharField(default="default", max_length=100, unique=True),
        ),
    ]
