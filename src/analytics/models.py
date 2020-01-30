from django.db import models
from shortner.models import shortURL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, shortURL):
            obj, created = self.get_or_create(short_url = instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    short_url   = models.OneToOneField(shortURL, on_delete=models.PROTECT)
    count       = models.IntegerField(default=0)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return"{i}".format(i = self.count)