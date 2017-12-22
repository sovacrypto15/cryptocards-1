from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptomonsters.settings')

# app = Celery('proj')
celery = Celery('cryptomonsters',
             broker='redis://localhost',
             # backend='db+postgresql://localhost:5432/async_tasks'
             backend='redis://localhost'
             )
CELERY_IMPORTS = ["mining.tasks"]
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django celery configs.
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@celery.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))