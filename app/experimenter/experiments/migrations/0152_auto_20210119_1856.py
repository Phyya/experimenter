# Generated by Django 3.1.5 on 2021-01-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0151_nimbusexperiment_risk_mitigation_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusdocumentationlink",
            name="title",
            field=models.CharField(
                choices=[
                    ("DS_JIRA", "Data Science Jira Ticket"),
                    ("DESIGN_DOC", "Experiment Design Document"),
                    ("ENG_TICKET", "Engineering Ticket (Bugzilla/Jira/GitHub)"),
                ],
                max_length=255,
            ),
        ),
    ]