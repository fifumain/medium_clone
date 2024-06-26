# Generated by Django 4.1.7 on 2024-02-24 18:21

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="about_me",
            field=models.TextField(
                default="say something about yourself", verbose_name="about me"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="city",
            field=models.CharField(
                default="Nairobi", max_length=180, verbose_name="city"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="country",
            field=django_countries.fields.CountryField(
                default="KE", max_length=2, verbose_name="country"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="O",
                max_length=20,
                verbose_name="gender",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+250784123456",
                max_length=30,
                region=None,
                verbose_name="phone number",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_photo",
            field=models.ImageField(
                default="/profile_default.png",
                upload_to="",
                verbose_name="profile photo",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="twitter_handle",
            field=models.CharField(
                blank=True, max_length=20, verbose_name="twitter handle"
            ),
        ),
    ]
