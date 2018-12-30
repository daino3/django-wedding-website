from django.core.management import BaseCommand
from guests.models import Party, Guest
import logging

LOG = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        count = Guest.objects.count()
        if raw_input('Really delete all {} guests?! (y/n):\n'.format(count)) == 'y':
            Party.objects.all().delete()
            LOG.info('guests deleted')
        else:
            LOG.info('canceled')
