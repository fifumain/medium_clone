from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

# Creating our own user manager


class CustomUserManager(BaseUserManager):

    # Method for validating email
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    # Method for creating a user
    def create_user(self, first_name, last_name, email, password, **extra_fields):

        if not first_name:
            raise ValueError(_("You must provide a first name"))

        if not last_name:
            raise ValueError(_("You must provide a last name"))

        # Check if an email is provided and validate it
        if email:
            # Normalizing email to a standard form (example@mail.com)
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("User must provide an email address"))

        # Create a new user with the provided information
        user = self.model(first_name=first_name, last_name=last_name,
                          email=email, **extra_fields)

        # Set the user's password
        user.set_password(password)

        # Set default values for 'is_staff' and 'is_superuser' if not provided
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        # Save the user to the database
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        # Set default values for 'is_staff' and 'is_superuser' if not provided
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have 'is_staff=True'"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have 'is_superuser=True'"))

        if not password:
            raise ValueError(_("Superuser must have a passsword"))

            # Check if an email is provided and validate it
        if email:
            # Normalizing email to a standard form (example@mail.com)
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Superuser must provide an email address"))

        user = self.create_user(first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user
