from celery import shared_task
from django.core.mail import send_mail
from .models import Email, Status


@shared_task
def send_emails_task(email_id):
    email = Email.objects.get(id=email_id)
    try:
        send_mail(
            email.task.subject,
            email.task.body,
            'admin@ar-ucheba.ru',
            [email.recipient],
            fail_silently=False,
        )
        #email.status = Status.objects.get(name='Отправлено')
        email.save()

        print("-------------------------------------")
        return f"Сообщение отправлено на "

    except Exception as e:

        return f"Не удалось отрпавить сообщение {str(e)}"
