# Generated by Django 4.2 on 2024-10-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0017_hobby_additionalinformation"),
        ("cv_template", "0011_cvanalysis_suggested_roles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cvtemplate",
            name="education",
            field=models.ManyToManyField(
                blank=True, related_name="cv_education", to="profiles.education"
            ),
        ),
        migrations.AlterField(
            model_name="cvtemplate",
            name="work_experience",
            field=models.ManyToManyField(
                blank=True,
                related_name="cv_work_experience",
                to="profiles.workexperience",
            ),
        ),
    ]
