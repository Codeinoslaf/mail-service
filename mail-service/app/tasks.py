from celery import shared_task
from django.core.mail import send_mail
from .models import EmailTask
import requests

@shared_task
def send_emails_task(task_id):
    email_task = EmailTask.objects.get(id=task_id)
    #recipients = [email.strip() for email in email_task.recipients.split(',')]
    recipients = [
        'nicksrnk@gmail.com',
        'tchernusho@gmail.com'
    ]
    
    try:
        send_mail(
            email_task.subject,
            email_task.body,
            'admin@ar-ucheba.ru',
            recipients,
            fail_silently=False,
        )
        email_task.status = 'completed'
        url = "http://127.0.0.1:8000/get/"

        payload = {}
        headers = {
            'Cookie': 'csrftoken=80poHXpVPtyB9GwI9Mr7hzHFGhIueLWa'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print("-------------------------------------")
        print(response.text)
    except Exception as e:
        email_task.status = f'failed: {str(e)}'
    
    email_task.save()
    return f"Email sent to {len(recipients)} recipients"