from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webhook.settings")

app = Celery("webhook")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.enable_utc = False
app.conf.timezone = "Asia/Almaty"
app.autodiscover_tasks()
