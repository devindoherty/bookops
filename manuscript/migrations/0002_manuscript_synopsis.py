# Generated by Django 4.2.10 on 2024-12-12 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manuscript", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="manuscript",
            name="synopsis",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
