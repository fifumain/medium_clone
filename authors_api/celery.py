import os

from celery import Celery
from django.conf import settings

# TODO: change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

app = Celery("authors_api")


app.config_from_object("django.conf:settings", namespace="CELERY")

# Heed that to make celery setup easier, and find task by auto
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
