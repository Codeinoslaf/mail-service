from celery import shared_task
from django.core.mail import send_mail
from .models import Email, Status


@shared_task
def send_emails_task(email_id):
    try:
        email = Email.objects.get(id=email_id)
        task = email.subject

        send_mail(
            task.subject,
            task.body,
            'admin@ar-ucheba.ru',
            email.recipient,
            fail_silently=False,
        )
        email.status = Status.objects.get(name='Отправлено')
        email.save()

        print("-------------------------------------")
        return f"Сообщение отправлено на {email.recipient}"

    except Exception as e:
        email.status = Status.objects.get(name='Ошибка!!!')
        email.save()
        return f"Не удалось отрпавить сообщение {str(e)}"
