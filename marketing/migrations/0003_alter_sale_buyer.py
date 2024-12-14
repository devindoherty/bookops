# Generated by Django 4.2.10 on 2024-12-14 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manuscript", "0003_manuscript_editor"),
        ("marketing", "0002_buyer_sale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="buyer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buys",
                to="manuscript.manuscript",
            ),
        ),
    ]