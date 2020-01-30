from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validator_url(val):
    url_validator = URLValidator()
    try:
        url_validator(val)
    except:
        raise ValidationError("Invalid URL")

def validate_dot_com(val):
    if not "com" in val:
        raise ValidationError("not end with com")
    return val