from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')
app.config_from_object(settings, namespace='CELERY')


app.conf.beat_schedule = {
    'working_at_every_5_minute': {
        'task': 'App.task.test_func',
        'schedule': crontab(minute='*/5')
    }
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
