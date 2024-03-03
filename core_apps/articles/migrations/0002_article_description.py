# Generated by Django 4.1.7 on 2024-03-03 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="description",
            field=models.CharField(
                default=django.utils.timezone.now,
                max_length=255,
                verbose_name="description",
            ),
            preserve_default=False,
        ),
    ]