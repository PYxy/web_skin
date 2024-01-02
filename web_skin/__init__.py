# 还要启动worker去执行任务   celery -A django_celery worker -l info -P eventlet
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery_server import app as celery_app

__all__ = ['celery_app']


import pymysql

pymysql.install_as_MySQLdb()



