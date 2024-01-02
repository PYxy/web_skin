from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from web_skin import celery_config

# set the default Django settings module for the 'celery' program.
# 设置django的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_skin.settings')

app = Celery('web_skin')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# 在settings中设置变量的时候要以CELERY_开头, namespace='CELERY'
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object(celery_config.CeleryConfig)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
