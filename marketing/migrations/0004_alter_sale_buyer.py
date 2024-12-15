# Generated by Django 4.2.10 on 2024-12-15 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("marketing", "0003_alter_sale_buyer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="buyer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buys",
                to="marketing.buyer",
            ),
        ),
    ]
