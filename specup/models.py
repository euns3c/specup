from django.db import models
from django.utils import timezone

class UserPointHistory(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now)
    user = models.ForeignKey('auth.User')
    delta = models.IntegerField(default=0)
    

class Admin_Point(models.Model):
    point = models.IntegerField(default=0)
    point_number = models.ManyToManyField(UserPointHistory)
