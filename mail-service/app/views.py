from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Email
from .tasks import send_emails_task

@api_view(['POST'])
def send_emails(request):
    recipients = request.POST.get('recipients', '123')
    subject = request.POST.get('subject', '123')
    body = request.POST.get('body', '123')

    email_task = Email.objects.create(
        recipients=recipients,
        subject=subject,
        body=body
    )

    # Запускаем асинхронную задачу
    send_emails_task.delay(email_task.id)

    return JsonResponse({'Статус': 'успешно', 'идентификатор задания': email_task.id})
    

def get_emails(request):

    return JsonResponse({'Статус': 'успешно'})

