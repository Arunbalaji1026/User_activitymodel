from django.db import models


# Create your models here.

class User(models.Model):
    real_name = models.CharField(max_length=50, null=True)

class ActivityPeriod(models.Model):
    real_name = models.CharField(max_length=50, null=True)
    tz_location = models.CharField(max_length=100, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

