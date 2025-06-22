Чтобы запустить приложения локально, проверяем settings.py:
1. 'HOST': 'localhost',       
        'PORT': '5433',
2. CELERY_BROKER_URL = 'amqp://user:pass@localhost:5672//'
db и rabbitmq -> должны быть подняты в docker'e
запускаем программу + в терминале прописываем:
3.celery -A mailservice worker --loglevel=info


Чтобы запустить приложения на сервере:

я сам пока не понял
