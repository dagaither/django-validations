from django.db import models
from django.core import validators as v
from .validators import validate_stroke, validate_distance, validate_record_date, validate_record_broken_date

class SwimRecord(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    team_name = models.CharField()
    relay = models.BooleanField()
    stroke = models.CharField(validators = [validate_stroke])
    distance = models.IntegerField(validators = [validate_distance])
    record_date = models.DateTimeField(validators = [validate_record_date])
    record_broken_date = models.DateTimeField(validators = [validate_record_broken_date])
