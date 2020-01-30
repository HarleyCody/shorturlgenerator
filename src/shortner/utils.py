import random, string
from django.conf import settings
SHORTURL_MIN = getattr(settings, "SHORTURL_MIN", 6)
def code_generator(size = SHORTURL_MIN, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shorturl(instance, size = SHORTURL_MIN):
    new_code = code_generator(size = size)
    shorturl = instance.__class__
    qs_exists = shorturl.objects.filter(shorturl = new_code).exists()
    if qs_exists:
        return create_shorturl(size = size)
    return new_code