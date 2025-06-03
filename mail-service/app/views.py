from django.shortcuts import render
from django.http import JsonResponse
from .models import Email
from .tasks import send_emails_task


def send_emails(request):

    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        body = request.POST.get('body', '')
        create_at = request.POST.get('create_at', '')

        email_task = Email.objects.create(
            subject=subject,
            body=body,
            create_at=create_at
        )

        # Запускаем асинхронную задачу
        send_emails_task.delay(email_task.id)

        return JsonResponse({'status': 'success', 'task_id': email_task.id})

    return render(request, 'templates/send_form.html') # ТАК?