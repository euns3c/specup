from django.db import models
from django.utils import timezone

class UserPointHistory(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now)
    user = models.ForeignKey('auth.User')
    delta = models.IntegerField(default=0)
