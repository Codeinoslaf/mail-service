from django.shortcuts import render
from django.http import JsonResponse
from .models import EmailTask
from .tasks import send_emails_task

def send_emails(request):
    if request.method == 'POST':
        recipients = request.POST.get('recipients', '')
        subject = request.POST.get('subject', '')
        body = request.POST.get('body', '')
        
        email_task = EmailTask.objects.create(
            recipients=recipients,
            subject=subject,
            body=body
        )
        
        # Запускаем асинхронную задачу
        send_emails_task.delay(email_task.id)
        
        return JsonResponse({'status': 'success', 'task_id': email_task.id})
    
    return render(request, 'mailer/send_form.html')