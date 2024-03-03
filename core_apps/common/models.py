from django.db import models
import uuid

# Create your models here.


# Timestamped model - abstract model, created to make next models work esasier, and less code
class TimeStampedModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract means that we can't use model to create objects
        abstract = True
        ordering = ("created_at", "updated_at")
