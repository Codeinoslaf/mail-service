Чтобы запустить приложения локально, проверяем settings.py:
                   1.
'HOST': 'localhost',       } для 
        'PORT': '5433',    } БД

                   2.
CELERY_BROKER_URL = 'amqp://user:pass@localhost:5672//' } celery

                   3.
db и rabbitmq -> должны быть подняты в docker'e

                   4.
запускаем программу + в терминале прописываем:
celery -A mailservice worker --loglevel=info

Чтобы запустить приложения на сервере:

я сам пока не понял
