import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import *
from .tasks import send_emails_task

@api_view(['POST'])
def send_emails(request):
    recipients = request.data['recipients']
    subject = request.data['subject']
    body = request.data['body']

    task = Task.objects.create(subject=subject, body=body)
    task.save()



    for element in recipients:

        if not Recipient.objects.filter(address=element).exists():
            Recipient.objects.create(address=element).save()


    email = Email.objects.create(
        recipient_list=json.dumps(recipients),
        task=task
    )


    email.save()
    # Запускаем асинхронную задачу
    send_emails_task.delay(email.id)

    return JsonResponse({'Статус': 'успешно', 'идентификатор задания': task.id})


