from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "periodic_send_email": {
        "task": "send_daily_report_email",
        "schedule": crontab(hour=20, minute=37),
        # 'schedule': 10.0,
    },
}
