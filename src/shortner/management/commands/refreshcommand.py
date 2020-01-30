from django.core.management.base import BaseCommand, CommandError
from shortner.models import shortURL

class Command(BaseCommand):
    helper = 'refreshes all shortURL shortcodes'

    # take input from commands as parameters
    def add_argument(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        return shortURL.objects.refresh_shorturl()
