from django.core.exceptions import ValidationError
import re
from django.utils import timezone

def validate_stroke(stroke):
    error_message = f"{stroke} is not a valid stroke"
    valid_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke in valid_strokes:
        return stroke
    else:
        raise ValidationError(error_message, params={'Current Value': stroke})
    
def validate_distance(distance):
    error_message = "Ensure this value is greater than or equal to 50."
    if distance >= 50:
        return distance
    else:
        raise ValidationError(error_message, params={'Current Value': distance})
    
def validate_record_date(record_date):
    error_message = "Can't set record in the future."
    now = timezone.now()
    if record_date <= now:
        return record_date
    else:
        raise ValidationError(error_message, params={'Current Value': record_date})

def validate_record_broken_date(record_broken_date):
    error_message = "Can't break record before record was set."
    now = timezone.now()
    if record_broken_date > now:
        return record_broken_date
    else:
        raise ValidationError(error_message, params={'Current Value': record_broken_date})
