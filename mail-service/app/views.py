import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import *
from .tasks import send_emails_task

@api_view(['POST'])
def send_emails(request):
    recipients = request.data.get('recipients', [])
    subject = request.data['subject']
    body = request.data['body']

    recipient_objects = []

    for email in recipients:
        recipient, _ = Recipient.objects.get_or_create(address=email)
        recipient.save()
        recipient_objects.append(recipient)

    task = Task.objects.create(subject=subject, body=body)
    task.save()
    email = Email.objects.create(task=task)

    email.recipient_list.set(recipient_objects)
    email.save()
    # Запускаем асинхронную задачу
    send_emails_task.delay(email.id)

    return JsonResponse({'status': 'success', 'task_id': task.id})