# Generated by Django 4.2.5 on 2023-11-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_remove_exhibits_exhibition_id_exhibits_exhibitions"),
    ]

    operations = [
        migrations.AddField(
            model_name="exhibitionhalls",
            name="date",
            field=models.DateField(null=True),
        ),
    ]
