from django.db import models
from .utils import code_generator, create_shorturl
from django.conf import settings
from .validator import validator_url, validate_dot_com
from django_hosts.resolvers import reverse
# Create your models here.
SHORTURL_MAX = getattr(settings, "SHORTURL_MAX", 15)

class shortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qsMain = super(shortURLManager, self).all(*args, **kwargs)
        qs = qsMain.filter(active=True)
        return qs

    def refresh_shorturl(self):
        qs = shortURL.objects.filter(id__gte = 1)
        new_codes = 0
        for q in qs:
            q.shorturl = create_shorturl(q)
            print(q.shorturl)
            q.save()
            new_codes += 1
        return "New codes made:{i}".format(i = new_codes)

class shortURL(models.Model):
    url         = models.CharField(max_length=220, validators=[validator_url, validate_dot_com])
    shorturl    = models.CharField(max_length=SHORTURL_MAX, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp    = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    objects = shortURLManager()

    def save(self, *args, **kwargs):
        if self.shorturl is None or self.shorturl == "":
            self.shorturl = create_shorturl(self)
        super(shortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("surl", kwargs={"shorturl": self.shorturl}, host = 'www', scheme='http')
        return url_path