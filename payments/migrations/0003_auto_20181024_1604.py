# Generated by Django 1.11.16 on 2018-10-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("payments", "0002_auto_20181024_1151")]

    operations = [
        migrations.RemoveField(model_name="payment", name="handled"),
        migrations.RemoveField(model_name="payment", name="paid"),
        migrations.AddField(
            model_name="payment",
            name="state",
            field=models.IntegerField(
                choices=[
                    (1, "New"),
                    (2, "Pending"),
                    (3, "Rejected"),
                    (4, "Accepted"),
                    (5, "Processed"),
                ],
                db_index=True,
                default=1,
            ),
        ),
    ]