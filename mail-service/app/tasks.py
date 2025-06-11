from celery import shared_task
from django.core.mail import send_mail
from .models import Email, Status


@shared_task
def send_emails_task(email_id):
    email = Email.objects.get(id=email_id)
    try:
        send_mail(
            subject=email.task.subject,
            message=email.task.body,
            from_email='admin@ar-ucheba.ru',
            recipient_list=[email.recipient],
            fail_silently=False,
        )
        email.status = Status.objects.get(id=1)
        email.save()

        return f"Письмо успешно отправлено"

    except Exception as e:
        email.status = Status.objects.get(id=2)
        email.save()
        return f"Ошибка при отправке письма {str(e)}"
