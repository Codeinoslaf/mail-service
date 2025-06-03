from celery_app import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mail-service.settings')

app = Celery('mail-service') # через - или _
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


