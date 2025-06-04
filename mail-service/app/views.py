from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import EmailTask
from .tasks import send_emails_task

def send_emails(request):
    if request.method == 'GET':
        recipients = request.POST.get('recipients', '123')
        subject = request.POST.get('subject', '123')
        body = request.POST.get('body', '123')
        
        email_task = EmailTask.objects.create(
            recipients=recipients,
            subject=subject,
            body=body
        )
        
        # Запускаем асинхронную задачу
        send_emails_task.delay(email_task.id)
        
        return JsonResponse({'status': 'success', 'task_id': email_task.id})
    
    return render(request, 'send_form.html')

def get_emails(request):
    if request.method == 'GET':

        data = json.loads(request.body)

        # name = data.get('name')
        # age = data.get('age')

        return JsonResponse({'status': 'success', 'received_data': data})
    return render(request, 'send_form.html')


