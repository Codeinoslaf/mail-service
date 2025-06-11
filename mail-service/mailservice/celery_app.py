import os
from celery import Celery

# Установите переменную окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailservice.settings')

# Создаем экземпляр Celery
app = Celery('mailservice')

# Загружаем настройки из settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи в приложениях Django
app.autodiscover_tasks()