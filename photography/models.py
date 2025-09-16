from django.db import models
from django.utils import timezone
# Create your models here.

class RefreshTime(models.Model):
    last_refreshed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Last refreshed: {self.last_refreshed}"
