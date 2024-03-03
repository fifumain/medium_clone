from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="1yNz57rQiT2vfaPaBYjtWy3Z6K2Jo6y3Er2My048jjUab7dNqvY"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
# USING celery for the email things
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# defailt hanlder in case all goes down -  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Some env settings for email
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@apiimperfect.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"
