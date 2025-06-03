from celery_app import shared_task
from django.core.mail import send_mail
from .models import Email


@shared_task
def send_emails_task(task_id):
    email_task = Email.objects.get(id=task_id)
    subject = [email.strip() for email in email_task.subject.split(',')]

    try:
        send_mail(
            email_task.subject,
            email_task.body,
            'noreply@yourdomain.com',
            subject,
            fail_silently=False,
        )
        email_task.status = 'completed'
    except Exception as e:
        email_task.status = f'failed: {str(e)}'

    email_task.save()
    return f"Email sent to {len(subject)} subject"