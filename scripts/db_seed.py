
from django.conf import settings
from django.apps import apps
from django.db import IntegrityError
import logging

log = logging.getLogger(__name__)

# python manage.py runscript db_seed
def run(*args):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    try:
        User.objects.create_superuser('admin@wedding.com', 'admin@wedding.com', 'password')
    except IntegrityError:
        log.warn('Already created...')
