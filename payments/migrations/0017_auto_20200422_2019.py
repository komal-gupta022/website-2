# Generated by Django 2.2.12 on 2020-04-22 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0016_auto_20200318_0955"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={"verbose_name": "Customer", "verbose_name_plural": "Customers"},
        ),
        migrations.AlterModelOptions(
            name="payment",
            options={
                "ordering": ["-created"],
                "verbose_name": "Payment",
                "verbose_name_plural": "Payments",
            },
        ),
    ]