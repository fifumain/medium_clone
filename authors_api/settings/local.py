from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="1yNz57rQiT2vfaPaBYjtWy3Z6K2Jo6y3Er2My048jjUab7dNqvY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["https://localhost:8080"]
