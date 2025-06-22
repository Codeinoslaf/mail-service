Чтобы запустить приложения локально, проверяем settings.py:

'HOST': 'localhost',       
        'PORT': '5433',

CELERY_BROKER_URL = 'amqp://user:pass@localhost:5672//'

db и rabbitmq -> должны быть подняты в docker'e

запускаем программу + в терминале прописываем:

celery -A mailservice worker --loglevel=info

Чтобы запустить приложения на сервере:

                 ?
