# Generated by Django 5.0.3 on 2024-04-08 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="cart_items",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.cart"
            ),
        ),
    ]
